<!--
title: AWS Python Scheduled Cron example in Python
description: This is an example of creating a function that runs as a cron job using the serverless 'schedule' event.
layout: Doc
-->
# AWS Python Scheduled Cron Example

This is an example of creating an error notification based on an error/exception in a Lambda function.

It uses an existing plugin created by "ACloudGuru" [serverless-plugin-aws-alerts](https://github.com/ACloudGuru/serverless-plugin-aws-alerts).

This very simple example triggers an exception in the "handler" function run by cron - A "ZeroDivisionError: division by zero" in order to trigger an "alert". The alert itself is defined in `serverless.yml` file, by creating an SNS topic.

## Example