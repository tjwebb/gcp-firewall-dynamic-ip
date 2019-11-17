# gcp-firewall-dynamic-ip
Auto-update GCP firewall rule for a dynamic source IP

## Install `checkip` function

```sh
gcloud functions deploy checkip --runtime python37 --trigger-http --memory=128MB
```

## Run local updater

```sh
gcloud beta auth application-default login
python update_firewall.py PROJECT_ID RULE_ID
```

Use cron to run this once per day, or whenever you change locations.
