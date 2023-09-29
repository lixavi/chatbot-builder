#!/bin/bash

# will print the error code and return from script
# will take two args.
# 1 = error code
# 2 = error message.

. ./scripts/variables.sh

function print_exit(){
    local error_code=${1}
    local error_msg=${2}
    echo -e "${RED}[Fail] ${error_msg} ${NOCOLOR}" 1>&2
    exit ${error_code}
}

function showBanner(){
    banner_file=${1}
    cat ${banner_file}
}

function showProgress(){
    local last_command_pid=${1}
    while ps | grep -i "${last_command_pid}" > /dev/null
    do 
        for i in '-' '\' '|' '/'
        do
            echo -ne "\b${i}"
            sleep 0.20
        done
        echo -en "\b"
    done
}

function installPackage() {
    local packageName=${1}
    apt-get install -y ${packageName} > /dev/null &
    last_command_pid=$!
    showProgress ${last_command_pid}
    wait ${last_command_pid} || print_exit 1 "not able to install ${packageName}."
}

function mavenTarget(){
    local mavenCmd=${1}
    mvn ${mavenCmd} > /dev/null &
    last_command_pid=$!
    showProgress ${last_command_pid}
    wait ${last_command_pid} || print_exit 1 "${mavenCmd} fail."
}

