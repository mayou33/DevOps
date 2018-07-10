# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-6-29
# Author Yo
# Email YoLoveLife@outlook.com

# OPS PUSH_MISSION
OPS_PUSH_MISSION_LACK_OF_KEY_OR_JUMPER = -3
OPS_PUSH_MISSION_UNREACHABLE = -2
OPS_PUSH_MISSION_FAILED = -1
OPS_PUSH_MISSION_WAIT_EXAM = 1
OPS_PUSH_MISSION_WAIT_UPLOAD = 2
OPS_PUSH_MISSION_WAIT_RUN = 3
OPS_PUSH_MISSION_RUNNING = 4
OPS_PUSH_MISSION_SUCCESS = 5
OPS_PUSH_MISSION_IMPORT_VAR = 6
OPS_PUSH_MISSION_IMPORT_TASKS = 7

# HOST
HOST_CLOSE = -2
# 此状态机器将不会参与到所有运维操作中
HOST_PAUSE = -1
HOST_CAN_BE_USE = 1

# GROUP
GROUP_PAUSE = -2
GROUP_UNREACHABLE = -1
GROUP_CAN_BE_USE = 1

# TIMELINE
# HOST
TIMELINE_HOST_CREATE = 10
TIMELINE_HOST_UPDATE = 11
TIMELINE_HOST_DELETE = 12
#GROUP
TIMELINE_GROUP_CREATE = 20
TIMELINE_GROUP_UPDATE = 21
TIMELINE_GROUP_DELETE = 22
# EXTENDUSER
TIMELINE_USER_CREATE = 30
TIMELINE_USER_UPDATE = 31
TIMELINE_USER_DELETE = 32
TIMELINE_USER_QRCODE = 33
# PMNGROUP
TIMELIME_PMNGROUP_CREATE = 40
TIMELINE_PMNGROUP_UPDATE = 41
TIMELINE_PMNGROUP_DELETE = 42
# KEY
TIMELINE_KEY_CREATE = 50
TIMELINE_KEY_UPDATE = 51
TIMELINE_KEY_DELETE = 52
# JUMPER
TIMELINE_JUMPER_CREATE = 60
TIMELINE_JUMPER_UPDATE = 61
TIMELINE_JUMPER_DELETE = 62
TIMELINE_JUMPER_FLUSH = 63
# META
TIMELINE_META_CREATE = 70
TIMELINE_META_UPDATE = 71
TIMELINE_META_DELETE = 72
# MISSION
TIMELINE_MISSION_CREATE = 80
TIMELINE_MISSION_UPDATE = 81
TIMELINE_MISSION_DELETE = 82
# VAR
TIMELINE_VAR_CREATE = 90
TIMELINE_VAR_UPDATE = 91
TIMELINE_VAR_DELETE = 92
# WORK
TIMELINE_WORK_CREATE = 100
TIMELINE_WORK_EXAM = 101
TIMELINE_WORK_CHECK = 102
TIMELINE_WORK_UPLOAD = 103
TIMELINE_WORK_RUN = 104
TIMELINE_WORK_DELETE = 105
TIMELINE_WORK_RESULTS = 106
# FILE
TIMELINE_UTILS_FILE_CREATE = 110
TIMELINE_UTILS_FILE_DELETE = 111
TIMELINE_UTILS_IMAGE_CREATE = 112
TIMELINE_UTILS_IMAGE_DELETE = 113
# DB
TIMELINE_DB_INSTANCE_CREATE = 120
TIMELINE_DB_INSTANCE_UPDATE = 121
TIMELINE_DB_INSTANCE_DELETE = 122
TIMELINE_DB_ROLE_CREATE = 123
TIMELINE_DB_ROLE_UPDATE = 124
TIMELINE_DB_ROLE_DELETE = 125
TIMELINE_DB_USER_CREATE = 126
TIMELINE_DB_USER_UPDATE = 127
TIMELINE_DB_USER_DELETE = 128
# SYSTYPE
TIMELINE_SYSTYPE_CREATE = 130
TIMELINE_SYSTYPE_UPDATE = 131
TIMELINE_SYSTYPE_DELETE = 132
# POSITION
TIMELINE_POSITION_CREATE = 140
TIMELINE_POSITION_UPDATE = 141
TIMELINE_POSITION_DELETE = 142
# DNS
TIMELINE_DNS_CREATE = 150
TIMELINE_DNS_UPDATE = 151
TIMELINE_DNS_DELETE = 152
