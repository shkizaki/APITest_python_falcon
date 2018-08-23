"# APITest_python_falcon" 

pip install falcon

#GET

curl http://localhost:8008/test_api?key=1

#POST

curl -d "key=1" http://localhost:8008/test_api
