# Microservice APIs

## Author: Jose Haro Peralta

[![image](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jose-haro-peralta/) [![image](	https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/JoseHaroPeralta)

Hello and welcome to the GitHub repository for my book [Microservice APIs](https://www.manning.com/books/microservice-apis)!

The book is conceived as a one-stop guide for learning how to design and build microservices and how to 
drive their integrations with APIs. There's a strong emphasis on best practices and applying principles 
and patterns that achieve loose coupling in your code. The book provides full examples of how to design 
and build a REST API and a GraphQL API.

In this repository, you'll find all the code examples used in the book.

- You can download two chapters of the book for free from this [link](https://www.microapis.io/resources/microservice-apis-in-python).
- And you can get a 40% discount using the following code: slperalta.

There's complementary material for the book in my blog at [microapis.io](https://microapis.io/blog)
and in my [YouTube channel](https://www.youtube.com/channel/UCtrp0AWmJJXb50zb12XxTlQ). If you find my
content useful, don't forget to subscribe, like, and share my content, as that helps me enormously to
continue producing content. I also run regularly [workshops](https://microapis.io/workshops) on topics related to this book.

This repository is structured around the book chapters. There's one folder per chapter. Each folder 
contains all the code you need to follow along with the examples for the corresponding chapter.

### Here's a brief outline of the book

#### Chapter 1: What are microservice web APIs?

It explains what microservices architecture is and how it differs from other architectural styles. It 
also explains what an API is, and it discusses the challenges of building and operating microservice APIs.
This chapter doesn't have code examples, so it's not reflected in this repository.

#### Chapter 2: A basic API implementation

Jump straight into the action! This chapter provides an early peek into the kind of work we're going to 
develop throughout the book. The chapter walks you through the steps of building an API using the popular 
framework [FastAPI](https://github.com/tiangolo/fastapi).

#### Chapter 3: Designing microservices

This chapter explains best practices, principles, and patterns for designing 
microservices platforms. The chapter uses the example of CoffeeMesh, a fictitious
on-demand coffee delivery platform that we use throughout the book. You'll learn
to decompose CoffeeMesh into microservices using two popular strategies: decomposition
by business capability and decomposition by subdomain.

#### Chapter 4: Principles of REST API design

Everything you always wanted to know about REST design principles and best practices, and how we leverage 
HTTP to design highly expressive REST APIs. You'll learn the most important principles
and patterns of REST API design, including proper use of HTTP methods and status codes,
how to design request and response payloads, and much more.

#### Chapter 5: Documenting REST APIs with OpenAPI

It introduces JSON Schema and OpenAPI, and teaches you how to use them to document REST APIs.

#### Chapter 6: Building REST APIs with Python

It provides a step-to-step guide for implementing REST APIs using [FastAPI](https://github.com/tiangolo/fastapi)
and [Flask](https://github.com/pallets/flask) with the 
[smorest plugin](https://github.com/marshmallow-code/flask-smorest) plugin.

#### Chapter 7: Service implementation patterns for microservices

Here you learn to implement the business and the data access layers of a service. You'll learn to apply 
important software development principles and patterns to achieve loose coupling in your code, and to keep it 
readable and maintainable. You'll learn about hexagonal architecture, the repository pattern, the 
unit of work pattern, and more. You'll also learn to use [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) to interact with a database
and [Alembic](https://github.com/sqlalchemy/alembic) to manage database schema changes from code. You'll
also learn to run API mock servers with [Prism](https://github.com/stoplightio/prism).

#### Chapter 8: Designing GraphQL APIs

Here you learn how GraphQL works and how to use the Schema Definition Language (SDL) to design and document 
GraphQL APIs. You'll learn about GraphQL's type system, how to define custom types, and how to design queries and mutations.

#### Chapter 9: Consuming GraphQL APIs

It explains how to interact with a GraphQL server. You'll go from performing simple queries to creating 
complex query statements with aliases, fragment, and parametrization. You'll also learn to run GraphQL 
mock servers, and you'll understand how GraphQL queries work behind the scenes.

#### Chapter 10: Building GraphQL APIs with Python

In this chapter you learn to implement a GraphQL using the excellent [Ariadne](https://github.com/mirumee/ariadne/) 
framework. You'll learn to create resolvers for GraphQL types, queries, and mutations, and to handle 
query parameters. You'll also learn to deal with custom types and optimise your queries using field resolves.

#### Chapter 11: API authorization and authentication

This is your one-stop guide to API authentication and authorization. If there's one thing you need to get 
right in your APIs, it's this. The chapter explains how Open Authorization 2.0 and OpenID Connect work. It
also the explains the main OAuth flows and when to use them. It explains what JSON Web Tokens (JWT) are,
how to inspect them, how to produce them, and how to validate them using [PyJWT](https://github.com/jpadilla/pyjwt).
It also explains how to integrate with an identity service provider such as [Auth0](https://auth0.com/).

#### Chapter 12: Testing and validating APIs

Here you learn how to test and validate your APIs. You'll learn about property-based testing, and how 
to apply it using Python's excellent property-based testing library [Hypothesis](https://github.com/HypothesisWorks/hypothesis). 
You'll also learn how to use the classic API testing framework [Dredd](https://github.com/apiaryio/dredd), 
and the more modern and excellent framework [Schemathesis](https://github.com/schemathesis/schemathesis).

#### Chapter 13: Dockerizing microservice APIs

In this chapter, you learn to run your microservice APIs with Docker. You'll learn to 
write a Dockerfile, build an image, and run the container. You'll also learn to
use Docker Compose to run multiple services together, including databases. Finally,
you'll learn to publish your Docker builds to a container registry (AWS ECR).

#### Chapter 14: Deploying Microservice APIs with Kubernetes

In the final chapter of the book, you'll learn to deploy your microservice APIs with Kubernetes. It's a very
packed chapter as there's a lot to learn and to take, but it's also one of the most gratifying chapters of 
the book. You'll learn to launch a Kubernetes cluster using [AWS EKS](https://aws.amazon.com/eks/), 
and to run your workloads with [AWS Fargate](https://aws.amazon.com/fargate/).
You'll also learn to use the [eksctl](https://eksctl.io/) command line tool to manage your Kubernetes 
infrastructure, and Kubernete's kubectl to manage deployments. You'll learn to launch a serverless Aurora 
database and to connect securely to it. You'll also learn to manage your application configuration securely.

#### Appendix A: Types of Web APIs and Protocols

Appendix A gives you an overview of some of the main protocols use nowadays 
to build APIs. You'll learn about the origin and evolution of APIs, going back to
the emergence of RPC, all the way to more modern protocols such as GraphQL and gRPC.
The discussion in this Appendix should help you make a more informed choice about 
which type of API you should use to integrate your services.

#### Appendix B: Managing an API's Lifecycle

This appendix teaches you some of the most common strategies for managing API
versioning. You'll also learn strategies for deprecating and retiring your APIs
and how to announce these events to your clients.

#### Appendix C: API Authorization with an Identity Provider

Appendix C teaches you how to integrate with an identity provider, like Auth0,
to manage access to your APIs. An identity provider is a service that manages the 
identity of your users, and it takes care of issuing authorization tokens. All you
need to do in your API is validating those tokens correctly, and this appendix 
teaches you how.
