# gcp-firewall-dynamic-ip
Auto-update GCP firewall rule for a dynamic source IP

## Install `checkip` function

```sh
gcloud functions deploy checkip --runtime python37 --trigger-http --memory=128MB
```

## Run local updater

```sh
python update_firewall.py
```
Use cron to run this once per day, or whenever you change locations
