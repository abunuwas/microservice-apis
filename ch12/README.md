# Chapter 12: Testing and validating APIs

Here you learn how to test and validate your APIs. You'll learn about property-based testing, and how 
to apply it using Python's excellent property-based testing library [Hypothesis](https://github.com/HypothesisWorks/hypothesis). 
You'll also learn how to use the classic API testing framework [Dredd](https://github.com/apiaryio/dredd), 
and the more modern and excellent framework [Schemathesis](https://github.com/schemathesis/schemathesis).

To keep things simple, the chapter recommends to test the orders API against 
the state of the implementation after chapter 6. However, it's also possible 
to continue straight from chapter 11. You don't need to make any special changes
to the code. You can simply copy the orders service from chapter 11 instead of 
chapter 6 and run the tests just the same. Just make sure you run the API with
the `AUTH_ON` flag set to `False` to make sure authorization doesn't get in the way
of the testing. In this chapter, we're validating that the API works as documented.
We're not running security tests.

One thing to bear in mind is that, after chapter 7, our service has a database, and 
therefore it'll be loaded with resources after running the test. Specially after running
the schemathesis test suite. My recommendation is start with a clean database every
time you run the tests. To do that, follow the following steps:

1. Delete the database file:

```bash
$ rm orders.db
```

2. Then recreate the database by running the migrations:

```bash
$ PYTHONPATH=`pwd` alembic upgrade heads
```

When running this kind of test against your own applications, bear this in mind too - 
they'll overload your test databases, so make sure you have a clean database in 
every test run.
