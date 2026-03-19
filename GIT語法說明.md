# 設定相關:<br>
git config --global user.name "(userName)"		設定帳號<br>
git config --global user.email "(e-mail)"		設定E-mail<br>
git config --list                               查看設定<br>
# git 設定:<br>
git clone		抓遠端儲存庫下來<br>
git init		Git 初始化	<br>
rm -rf .git		移除 Git<br>
# remote遠端設定:<br>
git remote add (origin) (git@~.git)             遠端連結<br>
git remote set-url (origin) (git@~.git)	-       修改遠端連結<br>
git remote remove (origin)	-	                移除遠端連結<br>
git remote -v		                            查詢遠端連結(URL)<br>
git push -u (origin) (master)		            推上遠端並綁定<br>