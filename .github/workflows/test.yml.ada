name: Img_Download


on:
  push:
    branches:
      - main
  schedule:
   - cron: '5 16 * * *'  # 本地时间每天的 1:00 执行
env:
    TZ: Asia/Shanghai

jobs:
   Img_download:
        runs-on: ubuntu-latest

        steps:
          - name: Checkout code
            uses: actions/checkout@v2
            with:
                fetch-depth: 0
          - name: Set up Python 3.8
            uses: actions/setup-python@v2
            with:
              python-version: '3.8'   
          - name: Install dependencies
            run: |
                python -m pip install --upgrade pip
                pip install -r ./requirements.txt
          - name: Run Bash script
            run: bash url.sh
          - name: Run script to download 
            run: |
              python ./download_image.py
          
          - name: commit
            run: |
                  git clone https://github.com/bgvioletsky/action1.git other_repo_temp
                  cp -r * other_repo_temp/
                  cd other_repo_temp
                  git config --local user.email "44770157@qq.com"
                  git config --local user.name "bgcode"
                  git pull
                  git add .
                  git commit -m "update $(date +'%Y-%m-%d %H:%M:%S')"  
          - name:  Push changes
            uses:    ad-m/github-push-action@master
            with:  
               github_token: ${{ secrets.MY_GIT_TOKEN }}
               branch: main
               
