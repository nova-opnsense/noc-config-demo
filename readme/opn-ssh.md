```bash

ssh-keygen
eval `ssh-agent -c`
ssh-add ~/.ssh/id_rsa

cat ~/.ssh/id_rsa.pub

```

nano ~/.ssh/config

```
Host *
  IgnoreUnknown AddKeysToAgent,UseKeychain
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_rsa

```

```
git config --global user.name "hai.nt"
git config --global user.email hai.nt@novaintechs.com

```