#!/bin/bash

ps -ef | grep 8222 | grep -v grep | awk '{print $2}' | xargs kill -9
