2. tree -f -L 2
3. cd /etc/
4. ls -a /etc/
cd
5. ls -lX
6. mkdir structure
7.  cd structure
mkdir 2018 2019 2020 2021 2022 2023
 cd 2018                                     
mkdir files pictures .passwords
cd 2019                                         
mkdir files pictures .passwords
cd 2020                                        
mkdir files pictures .passwords
cd 2021                                        
mkdir files pictures .passwords
cd 2022                                      
mkdir files pictures .passwords
cd 2023                                      
mkdir files pictures .passwords
8. cd structure                                   
touch {2018,2019,2020,2021,2022,2023}/files/data.md
9. touch {2018,2019,2020,2021,2022,2023}/pictures/picture.png
10. touch {2018,2019,2020,2021,2022,2023}/.passwords/.passwords.txt
11. touch -a -d "2024-01-01" {2018,2019,2020,2021,2022,2023}/files/data.md
12. touch -m -d "2024-06-10" {2018,2019,2020,2021,2022,2023}/.passwords/.passwords.txt
13. cd
cp -rf ~/structure/2023 ~/Downloads/2025
14. cd structure
 touch -m -d "2025-06-10" {2018,2019,2020,2021,2022,2023}/.passwords/.passwords.txt
 15. cd
 cp -Rp ~/Downloads/2025 ~/structure/  
 16. cd structure
 mv ~/structure/2025 ~/structure/2024
 17.mv ~/structure/2024/pictures/picture.png ~/structure/2024/pictures/image.png     
 mv ~/structure/2023/pictures/picture.png ~/structure/2023/pictures/image.png                                       ✔ │ 07:17:56 PM 
 ~  mv ~/structure/2022/pictures/picture.png ~/structure/2022/pictures/image.png                                       ✔ │ 07:18:07 PM 
 ~  mv ~/structure/2021/pictures/picture.png ~/structure/2021/pictures/image.png                                       ✔ │ 07:18:19 PM 
 ~  mv ~/structure/2020/pictures/picture.png ~/structure/2020/pictures/image.png                                       ✔ │ 07:18:28 PM 
 ~  mv ~/structure/2019/pictures/picture.png ~/structure/2019/pictures/image.png                                     1 ✘ │ 07:18:46 PM 
 ~  mv ~/structure/2018/pictures/picture.png ~/structure/2018/pictures/image.png                                       ✔ │ 07:18:57 PM
 18. cd
 mv ~/structure/2024 ~/structure/2018 ~/Documents/
 19/20 rm -r ~/Documents/2024
 21. cat > ~/structure/2019/files/data.md
 22. nano ~/structure/2020/files/data.md
23. code ~/structure/2021/files/data.md  
24. cat ~/structure/2020/files/data.md > ~/structure/2022/files/data.md
25. cd structure  
mkdir soft_links                                 ✔ │ 06:28:19 PM 
mkdir hard_links
26. ln -s ~/structure/2019 ~/structure/soft_links/2019         ✔ │ 06:30:15 PM 
 ln -s ~/structure/2020 ~/structure/soft_links/2020         ✔ │ 06:32:04 PM 
 ln -s ~/structure/2021 ~/structure/soft_links/2021         ✔ │ 06:32:36 PM 
 ln -s ~/structure/2022 ~/structure/soft_links/2022         ✔ │ 06:32:46 PM 
 ln -s ~/structure/2023 ~/structure/soft_links/2023   
 27. ln ~/structure/2020/files/data.md ~/structure/hard_links/data.md
cd structure
cd hard_links
 ln ~/structure/2021/.passwords/.passwords.txt
28. cd
cd structure
mkdir archives 
29. 
30. cd
mv ~/Downloads/image.jpg ~/structure/archives 
31. tar -cf ~/structure/archives/image.tar -C ~/structure/archives image.jpg
tar -czf ~/structure/archives/image.tar.gz -C ~/structure/archives image.jpg
tar -cjf ~/structure/archives/image.tar.bz2 -C ~/structure/archives image.jpg
32. zip -rP 1111 ~/structure/structure.zip ~/structure