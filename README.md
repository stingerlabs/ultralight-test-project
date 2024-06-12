# Ultralight Test Project

This project is a sample monorepo which shows how to use the [Ultralight GitHub Action](https://github.com/ultralightlabs/ultralight-github-action) to forward test execution reports and test protocol definitions to your Ultralight Design Controls instance.

[.github/workflows](.github/workflows) contains example GitHub workflow setups for test suites written in Playwright and pytest.  Other testing frameworks are supported as well, provided that the outputs for your test protocols and execution reports match the expected format for our GitHub action.

## Test Execution Reports
We support the JUnit XML format for test execution reports. Most testing frameworks provide mechanisms to output in JUnit, either in-built or via plugins. Every test case in the test execution output must include the ID of an existing Verification or Validation element in your Ultralight Design Controls instance.

The [next](/next) and [python](/python) apps in this sample project have been configured to output in JUnit, and have example test cases showing where the Ultralight Design Controls ID can be specified

## Test Protocol Definitions
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