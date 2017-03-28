import cv2
import numpy as np
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from typesHolder import cvTypes

class operation():
    """docstring for ClassName"""
    def __init__(self):
        pass
    
    actions = {}
    lastAction = None
    action = None
    tf = cvTypes()

    imgView = None

    def write_to_disk(self, img):
        cv2.imwrite(self.actions[self.action], img)

    def get_last_valid_action(self, actionName):
        actName = actionName
        actionNames = self.actions.keys()
        if actionName not in actionNames:
            actName = actionNames[len(actionNames)-1]
        return actName

    def update_img_view(self, actionName):
        self.imgView.source = self.actions[actionName]
        self.imgView.reload()

    def update_and_reload_image(self, actionName, imgName, img):
        self.actions[actionName] = imgName
        self.write_to_disk(img)
        self.update_img_view(actionName)

    def load_for_processing(self, actnName):
        actionName = self.get_last_valid_action(actnName)
        self.update_img_view(actionName)
        return cv2.imread(self.actions[actionName],cv2.IMREAD_UNCHANGED)

    def change_color_space(self, code):
        img = self.load_for_processing(self.lastAction)
        if code in self.tf.colorCodesMap.keys():
            try:
                img = cv2.cvtColor(img, self.tf.colorCodesMap[code])
                self.update_and_reload_image(self.action, '/tmp/visualOpencvtmp_color_space'+'.jpg', img)
            except Exception as e:
                self.show_error(e)
    def do_normalization(self, type, alpha, beta):
        img = self.load_for_processing(self.lastAction)
        try:
            if type == self.tf.normType[0]:
                img = cv2.normalize(img, img, alpha, beta, cv2.NORM_INF)
            elif type == self.tf.normType[1]:
                img = cv2.normalize(img, img, alpha, beta, cv2.NORM_L1)
            elif type == self.tf.normType[2]:
                img = cv2.normalize(img, img, alpha, beta, cv2.NORM_L2)
            elif type == self.tf.normType[3]:
                img = cv2.normalize(img, img, alpha, beta, cv2.NORM_MINMAX)
            self.update_and_reload_image(self.action, '/tmp/visualOpencvtmp_norm'+'.jpg', img)
        except Exception as e:
            self.show_error(e)

    def do_smoothing(self, type, ksize, sigmaColor, sigmaSpace):
        img = self.load_for_processing(self.lastAction)
        try:
            if type == self.tf.blurTypes[0]:
                kernel = np.ones((ksize,ksize),np.float32)/25
                img = cv2.filter2D(img,-1,kernel)
            elif type == self.tf.blurTypes[1]:
                img = cv2.blur(img,(ksize,ksize))
            elif type == self.tf.blurTypes[2]:
                img = cv2.boxFilter(img,(ksize,ksize))
            elif type == self.tf.blurTypes[3]:
                img = cv2.GaussianBlur(img,(ksize,ksize),0)
            elif type == self.tf.blurTypes[4]:
                img = cv2.medianBlur(img,ksize)
            elif type == self.tf.blurTypes[5]:
                img = cv2.bilateralFilter(img,ksize,sigmaColor,sigmaSpace)
            self.update_and_reload_image(self.action, '/tmp/visualOpencvtmp_smooth'+'.jpg', img)
        except Exception as e:
            self.show_error(e)

    def do_thresholding(self, thresholdType, min, max, simpleFunc, adaptiveFunc, channel='All', withOtsu=False, blockSize=3, C=0):
        img = self.load_for_processing(self.lastAction)
        try:
            if channel == '0':
                img=img[:,:,0]
            elif channel == '1':
                img=img[:,:,1]
            elif channel == '2':
                img=img[:,:,2]
            if thresholdType == self.tf.thresholdTypes[0]:
                if withOtsu:
                    ret,img = cv2.threshold(img,min,max,self.tf.simpleThresholdMethods[simpleFunc]+cv2.THRESH_OTSU)
                else :
                    ret,img = cv2.threshold(img,min,max,self.tf.simpleThresholdMethods[simpleFunc])
            else:
                img = cv2.adaptiveThreshold(img,max,self.tf.adaptiveThresholdMethods[adaptiveFunc],self.tf.simpleThresholdMethods[simpleFunc],blockSize,C)
            self.update_and_reload_image(self.action, '/tmp/visualOpencvtmp_thresh'+'.jpg', img)  
        except Exception as e:
            self.show_error(e)

    def do_morp(self, type, ksize, iter):
        img = self.load_for_processing(self.lastAction)
        try:
            kernel = np.ones((ksize,ksize),np.uint8)
            if type == self.tf.morpTypes[0]:
                img = cv2.erode(img,kernel,iterations = iter)
            elif type == self.tf.morpTypes[1]:
                img = cv2.dilate(img,kernel,iterations = iter)
            elif type == self.tf.morpTypes[2]:
                img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
            elif type == self.tf.morpTypes[3]:
                img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
            elif type == self.tf.morpTypes[4]:
                img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
            elif type == self.tf.morpTypes[5]:
                img = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
            elif type == self.tf.morpTypes[6]:
                img = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
            self.update_and_reload_image(self.action, '/tmp/visualOpencvtmp_morp'+'.jpg', img)
        except Exception as e:
            self.show_error(e)

    def do_image_Gradient(self, type, size, output_datatype, orient='x'):
        img = self.load_for_processing(self.lastAction)
        try:
            if type == self.tf.gradientTypes[0]:
                if orient == 'x':
                    img = cv2.Sobel(img,output_datatype,1,0,ksize=size)
                elif orient == 'y':
                    img = cv2.Sobel(img,output_datatype,0,1,ksize=size)
                else:
                    img = cv2.Sobel(img,output_datatype,1,0,ksize=size)
                    img = cv2.Sobel(img,output_datatype,0,1,ksize=size)
            elif type == self.tf.gradientTypes[1]:
                img = cv2.Laplacian(img,output_datatype)
            self.update_and_reload_image(self.action, '/tmp/visualOpencvtmp_grad'+'.jpg', img)    
        except Exception as e:
            self.show_error(e)

    def do_canny_edge_detection(self, min,max):
        img = self.load_for_processing(self.lastAction)
        try:
            img = cv2.Canny(img,min,max)
            self.update_and_reload_image(self.action, '/tmp/visualOpencvtmp_canny'+'.jpg', img)
        except Exception as e:
            self.show_error(e)

    def do_hough_line_transform(self, type, rho, theta, threshold, maxLineGap, minLineLength):
        if 'Edge Detection' not in self.actions.keys():
            self.show_error('Invalid Operation', 'Need edge detection done first')
            return
        img = cv2.imread(self.actions['Edge Detection'],cv2.IMREAD_UNCHANGED)
        to_draw = cv2.imread(self.actions['load'],cv2.IMREAD_UNCHANGED)
        self.imgView.source = self.actions['load']
        self.imgView.reload()
        try:
            if type == self.tf.houghTypes[0]:
                lines = cv2.HoughLines(img,rho,np.pi/theta,threshold)
                for rho,theta in lines[0]:
                    a = np.cos(theta)
                    b = np.sin(theta)
                    x0 = a*rho
                    y0 = b*rho
                    x1 = int(x0 + 1000*(-b))
                    y1 = int(y0 + 1000*(a))
                    x2 = int(x0 - 1000*(-b))
                    y2 = int(y0 - 1000*(a))
                    cv2.line(to_draw,(x1,y1),(x2,y2),(0,0,255),3)
            elif type == self.tf.houghTypes[1]:
                lines = cv2.HoughLinesP(img,rho,np.pi/theta,threshold,minLineLength,maxLineGap)
                for line in lines:
                    for x1,y1,x2,y2 in line:
                        cv2.line(to_draw,(x1,y1),(x2,y2),(0,0,255),3)
            self.update_and_reload_image(self.action, '/tmp/visualOpencvtmp_hough'+'.jpg', to_draw)
        except Exception as e:
            self.show_error(e)

    def show_error(self, error='Invalid Operation', msg='Invalid Operation'):
        layout = BoxLayout(orientation='vertical')
        label = Label(text=msg)
        btn = Button(text='Close',size_hint = (1,0.3))
        layout.add_widget(label)
        layout.add_widget(btn)
        popup = Popup(title='Error !', content=layout,size_hint=(None, None), size=(400, 400))
        btn.bind(on_press=popup.dismiss)
        popup.open()
