#!/bin/bash
curl -s https://jupiter.challenges.picoctf.org/problem/37821/ | grep substring | sed "s/') {/\n/g" | sed "s/[[:space:]]*if (checkpass.substring(\(split\*\|\)//" | sort -n | awk '{printf $4}' | tr -d "'"
