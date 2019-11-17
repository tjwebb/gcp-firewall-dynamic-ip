# gcp-firewall-dynamic-ip
Auto-update GCP firewall rule for a dynamic source IP

## Deploy `checkip` function

```sh
gcloud functions deploy checkip --runtime python37 --trigger-http --memory=128MB

availableMemoryMb: 128
entryPoint: checkip
httpsTrigger:
  url: https://us-central1-tjwebb-test-project.cloudfunctions.net/checkip
```

## Run local updater

```sh
gcloud beta auth application-default login
python update_firewall.py REGION PROJECT_ID RULE_ID
```

`REGION` is the region in which you deployed your `checkip` function.

### When rule is updated

```sh
python update_firewall.py us-central1 tjwebb-test-project test-rule

Your ip: 70.199.120.85
Replaced 70.199.148.46 with 70.199.120.85 in rule [ test-rule ]
Done.
```

### When already up-to-date

```sh
python update_firewall.py us-central1 tjwebb-test-project test-rule

Your ip: 70.199.120.85
Your firewall rule [ test-rule ] already allows your current IP [ 70.199.120.85 ]
Nothing to do.
```

Use cron to run this once per day, or whenever you change locations.
