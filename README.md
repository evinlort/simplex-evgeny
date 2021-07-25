Run with `docker`:
1. Build image with command `docker build -t IMAGE_NAME:latest .`
2. Run image with command `docker run -d -p 3000:PORT IMAGE_NAME` where PORT is the port you wish to run the application
3. To stop the app:
    1. Use `docker container ls` to get container name (Try in Linux `docker container ls | grep "simplex-evg" | awk -F'   ' '{print $7}'`)
    2. Execute `docker stop CONTAINER_NAME` (Try in Linux ``docker stop `docker container ls | grep "simplex-evg" | awk -F'   ' '{print $7}'` ``)
    
Run with `flask`
1. `pip3 install -r requirements.txt`
2. `export FLASK_APP=main.py`
3. `flask run --host=0.0.0.0 --port=3000`

Run with `python3`
1. `python3 main.py`
