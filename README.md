# Gmail_test
Для запуска Selenium GRID прописать в терминале 
java -jar PATH\selenium-server-4.1.2.jar hub
Затем откройте новое окно терминала, перейдите в папку с хром драйвером и создайте нод 
java -jar PATH\selenium-server-4.1.2.jar node
В териминале в папке с проектом пропишите 
pytest --alluredir result
для сохранения отчетов Allure в папку result

Чтобы просмотреть отчёты неоходимо установить Allure https://docs.qameta.io/allure/
В терминале в папке с проектом прописать 
allure serve result
