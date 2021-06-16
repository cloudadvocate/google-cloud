Watch full tutorial on the channel!!

Credits: https://devopscube.com/ansible-dymanic-inventry-google-cloud/

# Commands used in ansible dynamic inventory tutorial:

1. Install google-auth module using pip. I am using pip3.
    ```bash
    sudo pip3 install requests google-auth
    ```

2. Create a inventory directory. You can create this anywhere of your choice and change permissions.
    ```bash
    sudo mkdir -p /opt/ansible/inventory
    ```

3. Create the YAML inventory file (gcp.yaml) and copy the below contents and please change the file according to your project and service account:
``` yaml
---
plugin: gcp_compute
projects:
          - [your_gcp_account]
auth_kind: serviceaccount
service_account_file: /opt/ansible/inventory/service-account.json
keyed_groups:
  - key: labels
    prefix: label
  - key: zone
    prefix: zone
groups:
  remote: "'citrix' in (labels|list)"
  ```

4. Change directory permission
``` bash
sudo chmod -R 755 /opt/ansible
```

5. Test it!!
ansible-inventory --list -i gcp.yaml
