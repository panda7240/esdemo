# esdemo

   积累ES相关的所有操作

## 部署

* 创建虚拟环境

	```
	virtualenv venv 
	```

* 激活虚拟环境

	```
	source ./venv/bin/activate
	```

* 安装虚拟环境依赖包

	```
	pip install -r requirements.txt
	
	# 如果没有requirements.txt, 可以在运行程序的主机上直接运行如下命令生成该文件
	(venv) $ pip freeze >requirements.txt
	```

* 启动程序

	```
	python manage.py runserver --host 0.0.0.0
	
	# 查看帮助
	python manage.py runserver --help 
