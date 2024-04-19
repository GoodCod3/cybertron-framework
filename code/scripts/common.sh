#!/bin/bash

export FLASK_ENV="development"

export GOOGLE_APPLICATION_CREDENTIALS="${PWD}/auth/sa_finance.json"
export AUTH_USERNAME="sVcce__facTorZ"
export AUTH_PASSWORD="zL8nk3pTbRnfUdfe40Bco4b_Wt&QzoAZuz7J0lM7elFWTmphm!iRe4"

#export BIGQUERY_PROJECT="ms--finance-sap--pro--5ea5"
#export BIGQUERY_DATASET="SSFF_Finance"
export BIGQUERY_PROJECT="ms--finance-sap--pre--e426"
export BIGQUERY_DATASET="sfsf_finance"

#export SF_API_HOST="https://api55preview.sapsf.eu"
#export SF_API_USER="SFINTEGRACION@makingscieT1"
#export SF_API_PASS="S31d@r2022"
export SF_API_HOST="https://api55.sapsf.eu"
export SF_API_USER="SFINTEGRACION@makingscie"
export SF_API_PASS="S31d@r2022"

export SAP_API_HOST="https://makingscience-subaccount.it-cpi001-rt.cfapps.eu10.hana.ondemand.com"
export SAP_API_GET_EMPLOYEES_ENDPOINT="/http/MasterData/GetEmployeesWorkAgreement_P_V2"
export SAP_API_USER="sb-cee60cfe-3f9d-4970-8cb7-6b3cd2b1f5af!b93595|it-rt-makingscience-subaccount!b16077"
export SAP_API_PASS='85e17ed3-8924-47d7-a73c-48dd5e48344e$OyuQuPa8M-4AHL_jPeIVYiDqaEQFcpEsLWWeqFGxad0='
