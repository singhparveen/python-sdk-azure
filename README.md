# Azure Python SDK

Environment for working with Azure Python SDK

## Getting started

1. Ensure Python 3.8+ is installed on your system

2. Create an Azure Active Directory application

3. Create a secret for the application

4. Create a resource group

5. Assign the application to the _Contributor_ or _Reader_ role on the subscription or resource group

6. In `.env` fill in the `AZURE_CLIENT_ID` and `AZURE_CLIENT_SECRET` to match your Service Principal. Be sure to escape the JSON. Avoid using online tools to do this due to the sensitive nature of what you are escaping. The resulting `env` map will resemble:
    ```json
    {
        "AZURE_SUBSCRIPTION_ID": "12345678-1234-1234-1234-123456789012",
        "AZURE_CLIENT_ID": "abcdefab-abcd-abcd-abcd-abcdefabcdef",
        "AZURE_CLIENT_SECRET": "AL8)RxYQzCf./dF!y5EN13eqdg3T!qwh",
        "AZURE_TENANT_ID": "1234abcd-1234-1234-1234-1234abcd1234"
    }
    ```

7. Run `init.sh` to set up the environment for the Python environment

8. Add the following line to `.gitignore` to avoid committing any sensitive information:

    ```
    .vscode/
    ```

9. Develop and debug functions using the `Current File (Integrated Terminal)` configuration (press F5 with the file open)

## References

- [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk) (Unit test code in particular)
