import re

txt = """<dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div class="job-detail">
        职位描述：
        <br>1. 参与公司服务器端和工具的设计和开发
        <br>2. 优化服务器端设计，解决性能瓶颈
        <br>
        <br>职位要求：
        <br>1. 计算机相关专业本科及以上学历，3年以上工作经验。
        <br>2. 熟悉Python及基于Python的Web服务器端开发技术，熟悉至少一种主流Python Web框架，有Django项目经验者优先
        <br>3. 熟悉网络协议和主流前后端通信规范，了解Linux环境开发管理
        <br>4. 熟悉MySQL、PostgreSQL和主流NoSQL数据库
        <br>5. 具有较强的团队意识，高度的责任感，对工作积极严谨，勇于承担压力
        <br>工作地址
        </div>
    </dd>"""

res = re.sub(r'(\<[a-zA-Z0-9=/_\- \"]+\>)', "", txt)

print(res)