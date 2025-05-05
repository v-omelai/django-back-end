# Objectives

This project consists of two backend development exercises as part of a home assignment.

## Exercise 1: Blog Posts REST API

**Goal:** Implement a REST API to manage blog posts with in-memory data storage.

### Features

- CRUD operations for blog posts
- Pagination and sorting on listing endpoint
- Input validation and proper HTTP status codes
- REST design principles

## Exercise 2: External API Proxy

**Goal:** Implement a proxy service for a public API (e.g., JSONPlaceholder) with caching and rate limiting.

### Features

- Forwarding requests to `/posts` and `/posts/{id}` endpoints
- In-memory caching with TTL (30 seconds)
- Rate limiting (5 requests/minute per client IP)
- Input validation and structured responses
