import uuid
from datetime import datetime

from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import ValidationError

from api.schemas import (
    GetScheduledOrderSchema, ScheduleOrderSchema, GetKitchenScheduleParameters
)

blueprint = Blueprint('kitchen', __name__, description='Kitchen API')


schedules = []


def validate_schedule(schedule):
    errors = GetScheduledOrderSchema().validate(schedule)
    if errors:
        raise ValidationError(errors)


@blueprint.route('/kitchen/schedule')
class KitchenSchedules(MethodView):

    @blueprint.arguments(GetKitchenScheduleParameters, location='query')
    @blueprint.response(GetScheduledOrderSchema(many=True))
    def get(self, args):
        for schedule in schedules:
            validate_schedule(schedule)

        if not args:
            return schedules, 200

        query_set = [schedule for schedule in schedules]

        cancelled = args.get('cancelled')
        if cancelled is not None:
            if cancelled:
                query_set = [
                    schedule for schedule in schedules
                    if schedule['status'] == 'cancelled'
                ]
            else:
                query_set = [
                    schedule for schedule in schedules
                    if schedule['status'] != 'cancelled'
                ]

        since = args.get('since')
        if since is not None:
            query_set = [
                schedule for schedule in schedules
                if schedule['scheduled'] >= datetime.timestamp(since)
            ]

        limit = args.get('limit')
        if limit is not None and len(query_set > limit):
            query_set = query_set[:limit]

        return query_set, 200

    @blueprint.arguments(ScheduleOrderSchema)
    @blueprint.response(GetScheduledOrderSchema)
    def post(self, payload):
        payload['id'] = str(uuid.uuid4())
        payload['scheduled'] = datetime.now().timestamp()
        payload['status'] = 'pending'
        schedules.append(payload)
        validate_schedule(payload)
        return payload, 201


@blueprint.route('/kitchen/schedule/<schedule_id>')
class KitchenSchedule(MethodView):

    @blueprint.response(GetScheduledOrderSchema)
    def get(self, schedule_id):
        for schedule in schedules:
            if schedule['id'] == schedule_id:
                validate_schedule(schedule)
                return schedule, 200
        abort(404, description=f'Resource with ID {schedule_id} not found')

    @blueprint.arguments(ScheduleOrderSchema)
    @blueprint.response(GetScheduledOrderSchema)
    def put(self, payload, schedule_id):
        for schedule in schedules:
            if schedule['id'] == schedule_id:
                schedule.update(payload)
                validate_schedule(schedule)
                return schedule, 200
        abort(404, description=f'Resource with ID {schedule_id} not found')

    @blueprint.response()
    def delete(self, schedule_id):
        for index, schedule in enumerate(schedules):
            if schedule['id'] == schedule_id:
                schedules.pop(index)
                return schedule, 204
        abort(404, description=f'Resource with ID {schedule_id} not found')


@blueprint.response(GetScheduledOrderSchema)
@blueprint.route('/kitchen/schedule/<schedule_id>/cancel')
def cancel_schedule(schedule_id):
    for schedule in schedules:
        if schedule['id'] == schedule_id:
            schedule['status'] = 'cancelled'
            validate_schedule(schedule)
            return schedule, 200
    abort(404, description=f'Resource with ID {schedule_id} not found')
