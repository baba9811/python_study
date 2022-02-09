"""
파일 : day12-01-class_quiz
개요 : 응용문제 3번
page : 271
"""

'''
3. 지시사항에 따라 노래 제목과 장르 정보를 저장할 수 있는
Song 클래스와 가수 이름과 대표곡 정보를 저장할 수 있는 Singer 클래스를 구현하세요.

[ 지시사항 ]
- 다음과 같은 방법으로 song과 singer 인스턴스를 생성하고,
필요한 정보를 저장한 뒤 그 정보를 출력하세요.
    # song 인스턴스 생성
    song = Song()
    song.set_song('취중진담', '발라드')
    
    # singer 인스턴스 생성
    singer = Singer()
    singer.set_singer('김동률')
    
    # singer의 대표곡 지정
    singer.hit_song(song)
    
    # singer 정보 출력
    singer.print_singer()
    
- Song 클래스는 다음 메소드를 반드시 가져야함.
    ㄴ set_song() : 노래 제목, 장르를 저장
- Singer 클래슨느 다음 메소드를 반드시 가져야함.
    ㄴ set_singer() : 가수 이름을 저장
    ㄴ hit_song() : 대표곡 저장
    ㄴ print_singer() : 가수 이름과 대표곡 제목과 장르 출력
    
[ 출력 ]
가수이름 : 김동률
노래제목 : 취중진담(발라드)
'''

class Song:

    # 제목, 장르 저장
    def set_song(self, title, genre):
        self.title = title
        self.genre = genre

class Singer:

    def set_singer(self, singer):
        self.singer = singer

    # 추가!
    def hit_song(self, song):
        self.song = song

    def print_singer(self):
        print(f'가수이름 : {self.singer}')
        # 추가!!
        print(f'노래제목 : {self.song.title}({self.song.genre})')

# song 인스턴스 생성
song = Song()
song.set_song('취중진담', '발라드')

# singer 인스턴스 생성
singer = Singer()
singer.set_singer('김동률')

# singer의 대표곡 지정
singer.hit_song(song)

# singer 정보 출력
singer.print_singer()











