#!/bin/bash
# Setup that demonstrates run_setup_sh execution. Touches a sentinel file
# so the agent author can verify setup actually ran on their machine.
echo "setup.sh ran for starfire-test-plugin at $(date)" > /tmp/sf-plugin-test-setup-ran
