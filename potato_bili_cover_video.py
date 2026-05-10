from manim import *

class Potato_Bili_Cover_Intro(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE  # 设置相机的背景颜色为白色

        self.play(
            self.camera.frame.animate.shift(UP*2.8888).set(width = 8),
        )
        self.wait(1)
        
        image_potato = ImageMobject(r"./potato_pfp.jpg")
        image_potato.shift(UP*1.2222)
        image_potato.scale(0.8888)  # 放大图片（可选
        
        tex_potato = Tex(r"WHITE POTATO", color = BLACK).next_to(image_potato, UP)
        tex_potato.shift(DOWN*0.2222)
        self.play(
            Write(tex_potato),
            run_time = 2.8888
        )
        self.wait(0.2222)
        self.play(
            FadeIn(image_potato),
            self.camera.frame.animate.shift(DOWN*0.8888).set(width = 14),
        )
        self.wait(0.2222)

        tex_selected = ImageMobject(r"./_tex精选作品集.png").set_opacity(0.6666)
        tex_selected.next_to(image_potato, DOWN)
        tex_selected.shift(UP*0.2222)
        self.play(
            FadeIn(tex_selected),
            self.camera.frame.animate.shift(DOWN*0.8888),
        )
    
    # manim -pqh potato_intro.py --disable_caching

        self.wait(2.2222)
        
        
if __name__ == "__main__":
    scene = Potato_intro(camera_config={"background_color": WHITE})
    scene.render()