"""
파일명 : module4
import를 사용해서 모듈을 가져올때 별명을 사용해보자.
"""
import converter as cvt

# converter 모듈을 사용할건데!!!!
# 이 모듈명을 cvt로 별명을 지어주고 쓸꺼야!!!!
# converter == cvt

print(cvt.int_to_str(1, 2, 3, 4, 5))

# from 모듈 import 도 별명을 지어줄 수 있음!!!!!!
from converter import int_to_str as its
print(its(1, 2, 3, 4, 5, 6))

# as를 이용해서 별명을 짓는건 많이 사용됨!!!!!
# 알아둬야 선임이 쓸때 파악하기 쉬움









