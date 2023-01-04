VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "任务管理器 v1.0.0"
   ClientHeight    =   6600
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   7110
   LinkTopic       =   "Form1"
   ScaleHeight     =   6600
   ScaleWidth      =   7110
   StartUpPosition =   3  '窗口缺省
   Begin VB.ComboBox Combo10 
      Height          =   300
      Left            =   4800
      TabIndex        =   22
      Text            =   "Combo10"
      Top             =   240
      Width           =   1335
   End
   Begin VB.VScrollBar VScroll1 
      Height          =   3135
      Left            =   5640
      TabIndex        =   20
      Top             =   840
      Width           =   495
   End
   Begin VB.Frame Frame2 
      Caption         =   "当日任务"
      Height          =   3255
      Left            =   360
      TabIndex        =   19
      Top             =   720
      Width           =   5295
      Begin VB.CheckBox Check1 
         Caption         =   "Task1"
         Height          =   375
         Left            =   360
         TabIndex        =   21
         Top             =   720
         Width           =   4575
      End
   End
   Begin VB.ComboBox Combo9 
      Height          =   300
      Left            =   2760
      TabIndex        =   17
      Text            =   "Combo9"
      Top             =   240
      Width           =   855
   End
   Begin VB.ComboBox Combo8 
      Height          =   300
      Left            =   1920
      TabIndex        =   16
      Text            =   "Combo8"
      Top             =   240
      Width           =   735
   End
   Begin VB.ComboBox Combo7 
      Height          =   300
      Left            =   960
      TabIndex        =   15
      Text            =   "Combo7"
      Top             =   240
      Width           =   855
   End
   Begin VB.Frame Frame1 
      Caption         =   "添加新任务"
      Height          =   2175
      Left            =   360
      TabIndex        =   0
      Top             =   4200
      Width           =   6255
      Begin VB.TextBox Text2 
         Height          =   735
         Left            =   960
         TabIndex        =   13
         Text            =   "Text2"
         Top             =   1320
         Width           =   3495
      End
      Begin VB.ComboBox Combo6 
         Height          =   300
         Left            =   3960
         TabIndex        =   12
         Text            =   "Combo6"
         Top             =   720
         Width           =   495
      End
      Begin VB.ComboBox Combo5 
         Height          =   300
         Left            =   3360
         TabIndex        =   11
         Text            =   "Combo5"
         Top             =   720
         Width           =   495
      End
      Begin VB.ComboBox Combo4 
         Height          =   300
         Left            =   2640
         TabIndex        =   10
         Text            =   "Combo4"
         Top             =   720
         Width           =   615
      End
      Begin VB.ComboBox Combo3 
         Height          =   300
         Left            =   1800
         TabIndex        =   9
         Text            =   "Combo3"
         Top             =   720
         Width           =   735
      End
      Begin VB.ComboBox Combo2 
         Height          =   300
         Left            =   1080
         TabIndex        =   8
         Text            =   "Combo2"
         Top             =   720
         Width           =   615
      End
      Begin VB.ComboBox Combo1 
         Height          =   300
         Left            =   4800
         TabIndex        =   7
         Text            =   "Combo1"
         Top             =   240
         Width           =   1215
      End
      Begin VB.CommandButton Command1 
         Caption         =   "添加"
         Height          =   495
         Left            =   4800
         TabIndex        =   3
         Top             =   960
         Width           =   975
      End
      Begin VB.TextBox Text1 
         Height          =   375
         Left            =   960
         TabIndex        =   1
         Text            =   "Text1"
         Top             =   240
         Width           =   3015
      End
      Begin VB.Label Label5 
         Caption         =   "备注"
         Height          =   375
         Left            =   240
         TabIndex        =   14
         Top             =   1320
         Width           =   735
      End
      Begin VB.Label Label4 
         Caption         =   "优先级"
         Height          =   375
         Left            =   4200
         TabIndex        =   6
         Top             =   240
         Width           =   855
      End
      Begin VB.Label Label3 
         Caption         =   "结束时间"
         Height          =   255
         Left            =   240
         TabIndex        =   5
         Top             =   1080
         Width           =   735
      End
      Begin VB.Label Label2 
         Caption         =   "开始时间"
         Height          =   375
         Left            =   240
         TabIndex        =   4
         Top             =   720
         Width           =   735
      End
      Begin VB.Label Label1 
         Caption         =   "任务名"
         Height          =   375
         Left            =   240
         TabIndex        =   2
         Top             =   240
         Width           =   1095
      End
   End
   Begin VB.Label Label7 
      Caption         =   "排序依据"
      Height          =   375
      Left            =   3840
      TabIndex        =   23
      Top             =   240
      Width           =   855
   End
   Begin VB.Label Label6 
      Caption         =   "日期"
      Height          =   375
      Left            =   360
      TabIndex        =   18
      Top             =   240
      Width           =   855
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Form_Load()

End Sub
