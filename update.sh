#!/bin/bash

QC_link='https://docs.google.com/spreadsheets/d/e/2PACX-1vSlsad634tbtTSNH9WGdCBiB00qNa_CO_c0wAxdqsGZqB01imqEzcG-Nba5f7PkvTrHsASLRJYeTx98/pub?output=csv'
demographics_link='https://docs.google.com/spreadsheets/d/e/2PACX-1vQl_ffOrkytiq6wy5eL5CBoi2pAcV7tZoGziXvFPctNmydBSMyovon8TxU9nly7cBHmbLPXFkcbR0H7/pub?gid=599005683&single=true&output=csv'

curl -L -o data/QC_data.csv "${QC_link}"
curl -L -o data/demographic_data.csv "${demographics_link}"
