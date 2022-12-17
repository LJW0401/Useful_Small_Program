VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "辅助着陆"
   ClientHeight    =   3375
   ClientLeft      =   120
   ClientTop       =   450
   ClientWidth     =   4560
   LinkTopic       =   "Form1"
   ScaleHeight     =   3375
   ScaleWidth      =   4560
   StartUpPosition =   3  '窗口缺省
   Begin VB.TextBox Text9 
      Height          =   270
      Left            =   840
      TabIndex        =   24
      Text            =   "Text9"
      Top             =   2280
      Width           =   1575
   End
   Begin VB.TextBox Text8 
      Height          =   270
      Left            =   960
      TabIndex        =   20
      Text            =   "Text8"
      Top             =   2760
      Width           =   1455
   End
   Begin VB.TextBox Text7 
      Height          =   270
      Left            =   1080
      TabIndex        =   18
      Text            =   "Text7"
      Top             =   1920
      Width           =   1335
   End
   Begin VB.TextBox Text6 
      Height          =   270
      Left            =   720
      TabIndex        =   15
      Text            =   "Text6"
      Top             =   1560
      Width           =   1695
   End
   Begin VB.TextBox Text5 
      Height          =   270
      Left            =   720
      TabIndex        =   11
      Text            =   "Text5"
      Top             =   1200
      Width           =   1695
   End
   Begin VB.TextBox Text4 
      Height          =   270
      Left            =   1320
      TabIndex        =   8
      Text            =   "Text4"
      Top             =   840
      Width           =   1095
   End
   Begin VB.TextBox Text3 
      Height          =   270
      Left            =   1320
      TabIndex        =   5
      Text            =   "Text3"
      Top             =   360
      Width           =   615
   End
   Begin VB.TextBox Text2 
      Height          =   270
      Left            =   360
      TabIndex        =   3
      Text            =   "Text2"
      Top             =   360
      Width           =   735
   End
   Begin VB.TextBox Text1 
      Height          =   270
      Left            =   360
      TabIndex        =   1
      Text            =   "Text1"
      Top             =   120
      Width           =   1575
   End
   Begin VB.Label unit 
      Caption         =   "(t)"
      Height          =   255
      Index           =   6
      Left            =   2520
      TabIndex        =   25
      Top             =   2280
      Width           =   735
   End
   Begin VB.Label Label10 
      Caption         =   "当前质量"
      Height          =   255
      Left            =   0
      TabIndex        =   23
      Top             =   2280
      Width           =   1095
   End
   Begin VB.Label Label9 
      Caption         =   "本程序忽略空气阻力影响及燃料消耗影响进行估算"
      Height          =   1095
      Left            =   3360
      TabIndex        =   22
      Top             =   120
      Width           =   1095
   End
   Begin VB.Label unit 
      Caption         =   "(m)"
      Height          =   255
      Index           =   5
      Left            =   2520
      TabIndex        =   21
      Top             =   2760
      Width           =   855
   End
   Begin VB.Label Label8 
      Caption         =   "点火高度 >"
      ForeColor       =   &H000080FF&
      Height          =   255
      Left            =   0
      TabIndex        =   19
      Top             =   2760
      Width           =   1215
   End
   Begin VB.Label Label7 
      Caption         =   "燃料消耗速率"
      Height          =   375
      Left            =   0
      TabIndex        =   17
      Top             =   1920
      Width           =   1335
   End
   Begin VB.Label unit 
      Caption         =   "(kN)"
      Height          =   255
      Index           =   4
      Left            =   2520
      TabIndex        =   16
      Top             =   1560
      Width           =   735
   End
   Begin VB.Label Label6 
      Caption         =   "最大推力"
      Height          =   255
      Left            =   0
      TabIndex        =   14
      Top             =   1560
      Width           =   975
   End
   Begin VB.Label unit 
      Caption         =   "(m/s)"
      Height          =   255
      Index           =   3
      Left            =   2520
      TabIndex        =   13
      Top             =   1200
      Width           =   735
   End
   Begin VB.Label unit 
      Caption         =   "(m)"
      Height          =   255
      Index           =   2
      Left            =   2520
      TabIndex        =   12
      Top             =   840
      Width           =   615
   End
   Begin VB.Label unit 
      Caption         =   "(m^3/s^2)"
      Height          =   255
      Index           =   1
      Left            =   2040
      TabIndex        =   10
      Top             =   360
      Width           =   1215
   End
   Begin VB.Label unit 
      Caption         =   "(km)"
      Height          =   255
      Index           =   0
      Left            =   2040
      TabIndex        =   9
      Top             =   120
      Width           =   615
   End
   Begin VB.Label Label5 
      Caption         =   "当前速度"
      Height          =   255
      Left            =   0
      TabIndex        =   7
      Top             =   1200
      Width           =   1215
   End
   Begin VB.Label Label4 
      Caption         =   "当前离地表高度"
      Height          =   375
      Left            =   0
      TabIndex        =   6
      Top             =   840
      Width           =   1575
   End
   Begin VB.Label Label3 
      Caption         =   "E+"
      Height          =   255
      Left            =   1080
      TabIndex        =   4
      Top             =   360
      Width           =   495
   End
   Begin VB.Label Label2 
      Caption         =   "R"
      Height          =   255
      Left            =   0
      TabIndex        =   2
      Top             =   120
      Width           =   495
   End
   Begin VB.Label Label1 
      Caption         =   "GM"
      Height          =   375
      Left            =   0
      TabIndex        =   0
      Top             =   360
      Width           =   855
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
'初始化-------------------------------------------------------------------------------
Private Sub Form_Load()
Text1.Text = "600": Text2.Text = "3.532": Text3.Text = "12": Text4.Text = "": Text5.Text = ""
Text6.Text = "": Text7.Text = "": Text8.Text = "": Text9.Text = ""
End Sub
'*************************************************************************************
'Model-1:计算点火高度-----------------------------------------------------------------
Function CFH(GM As Single, R As Single, H As Single, v0 As Single, F As Single, M As Single) As Integer
Dim T As Single, g As Single
g = GM / (R ^ 2)
a = F / M - g
h2 = (v0 ^ 2 + 2 * g * H) / (2 * (a + g))
CFH = Int(h2 + 0.5)
End Function
'*************************************************************************************

Private Sub Label8_Click()
Dim R As Single, GM As Single, H As Single, v0 As Single, F As Single, M As Single
R = Val(Text1.Text) * 1000
GM = Val(Text2.Text) * 10 ^ Val(Text3.Text)
H = Val(Text4.Text)
v0 = Val(Text5.Text)
F = Val(Text6.Text) * 1000
M = Val(Text9.Text) * 1000
h0 = CFH(GM, R, H, v0, F, M)
Text8.Text = CStr(h0)
End Sub
