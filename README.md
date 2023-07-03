# icard

A virtual payment solution developed during inCode 2023 Hackathon.

## Theme : Ideal Ride Hailing

What the ideal ride-hailing service should look like.

Analyze your experience of city rides, traveling between cities, or delivering goods.

Think about what you are missing, come up with the perfect service, and implement your idea at our hackathon.

## My Solution

``icard`` a virtual in-app payment method was developed to make payment of service fast, easy and accessible.

## Figma Prototype

[Prototype Link](https://www.figma.com/proto/tqzf8MOUuXfnRJceFqfrVy/UI%2FUX?type=design&node-id=65-2738&t=4PAOT641FQ74ky0d-1&scaling=scale-down&page-id=0%3A1&starting-point-node-id=65%3A2735&mode=design)

![Image of Figma Prototype](https://github.com/Danny10ison/icard/blob/main/inDrive-iCard-UIUX.png)

## API Docs

Once your api is running on local machine, follow the links
below to interact with the api.

[Redoc Documentation](http://localhost:8000/redoc)

![Image of Redoc on local](https://github.com/Danny10ison/icard/blob/main/inDrive-iCard-FastAPI_docs.png)

[Swagger UI](http://127.0.0.1:8000/docs)

## Start

- Create a virtual environment -NIX OS

  ```bash
  python3 -m venv env
  ```

  Windows

  ```powershell
  python.exe -m venv env
  ```

- Activate the virtual environment
  -NIX OS

  ```bash
  env/bin/activate
  ```

  Windows

  ```powershell
  .\env\Scripts\activate.bat
  ```

- Install all required packages -NIX OS

  ```bash
  pip install -r requirements.txt
  ```

  Windows

  ```powershell
  .\env\Scripts\pip.exe install -r .\requirements.txt
  ```

## Run the app

-NIX

```bash
uvicorn main:app
```

Windows

```powershell
.\env\Scripts\python.exe -m uvicorn main:app
```
