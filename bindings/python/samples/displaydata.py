from samplebase import SampleBase
from rgbmatrix import graphics
import time
from TIC_API import *
from dotenv import load_dotenv
import os

load_dotenv()
Normal = os.environ.get("Normal")
Warning = os.environ.get("Warning")


class RunDisplay(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunDisplay, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text")
        
    def setColor(self, temp):
        Red = graphics.Color(255, 0, 0)
        Yellow = graphics.Color(255, 255, 0)
        Green = graphics.Color(0, 255, 0)
        
        if float(temp) <= float(Normal):
            textColor = Green
        elif float(temp)>float(Normal) and float(temp)<float(Warning):
            textColor = Yellow
        else:
            textColor = Red
        
        return textColor

    def run(self):
        try:
            textColor = graphics.Color(0, 255, 0)
            font = graphics.Font()
            font.LoadFont("../../../fonts/7x13.bdf")
            
        
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            
            while True:
                # 열화상 데이터 호출
                TIC_API.getInstance().SetFilePath("/home/icns/Desktop/TIC_Soft/")
                TmperatureList_10x10 = TIC_API.getInstance().GetTemperatureList(PixelType.TenByTen.value, "TIC_Data")
                GetDetectFireList = TIC_API.getInstance().GetAllJsonData("DetectFireList") # Get DetetctFireList Data. return 2 Dimensional Array

 #               for i in len(GetDetectFireList["DetectFireList"]):
 #                   print(GetDetectFireList["DetectFireList"][i][0] , GetDetectFireList["DetectFireList"][i][1])

                datas = GetDetectFireList["DetectFireList"]
                #currunt_temp1 = str(round(TmperatureList_10x10[0][0])) # 1번 화구
                #currunt_temp2 = str(round(TmperatureList_10x10[0][1])) # 2번 화구
                #currunt_temp3 = str(round(TmperatureList_10x10[0][2])) # 3번 화구
                currunt_temp1 = str(112) # 1번 화구
                currunt_temp2 = str(108) # 2번 화구
                currunt_temp3 = str(117) # 3번 화구
                
            
                # display1 = f'{currunt_temp1}'
                # display2 = f'{currunt_temp2}'
                # display3 = f'{currunt_temp3}'
                # print(type(display1))
            
                pos1 =(offscreen_canvas.width -len(currunt_temp1)*7)//2
                pos2 =(offscreen_canvas.width -len(currunt_temp2)*21)//2
                pos3 =(offscreen_canvas.width -len(currunt_temp3))//3*2
        
                
            

                
                offscreen_canvas.Clear()
                ren = graphics.DrawText(offscreen_canvas, font, pos1, 11, self.setColor(currunt_temp1), currunt_temp1)
                ren = graphics.DrawText(offscreen_canvas, font, pos2, 25, self.setColor(currunt_temp2), currunt_temp2)
                ren = graphics.DrawText(offscreen_canvas, font, pos3, 25, self.setColor(currunt_temp3), currunt_temp3)

                time.sleep(1)
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
        except Exception:
            import traceback
            traceback.print_exc()
            


# Main function
if __name__ == "__main__":
    run_display = RunDisplay()
    if (not run_display.process()):
        run_display.print_help()
