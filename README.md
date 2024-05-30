# Ultralight Test Project

This project is a monorepo which shows how to interact with the Ultralight GitHub Action. See `.github/workflows` for exact mechanisms.

Overall - the Ultralight GitHub Action can be used to forward test execution results as well as test protocols to your Ultralight instance.

## Test Executions
We support the JUnit XML format to parse through your reported test executions. Most testing frameworks provide mechanisms to do this, either in-built or via plugins. This repository shows examples of how to work with Playwright and Pytest to generate JUnit XML files which can then be forwarded to Ultralight.

## Test Protocols
Each test case must be written in the following format:
```yaml
ultralight-test-id: number
title: string
description: string
steps:
    - step: string
      acceptance_criteria: string
    - step: string
      acceptance_criteria: string
```