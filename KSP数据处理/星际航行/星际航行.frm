VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "星际航行"
   ClientHeight    =   3330
   ClientLeft      =   120
   ClientTop       =   450
   ClientWidth     =   4335
   LinkTopic       =   "Form1"
   ScaleHeight     =   3330
   ScaleWidth      =   4335
   StartUpPosition =   3  '窗口缺省
   Begin VB.Frame Frame1 
      Caption         =   "霍曼转移"
      Height          =   3015
      Left            =   120
      TabIndex        =   0
      Top             =   120
      Width           =   3975
      Begin VB.TextBox Text5 
         Height          =   270
         Left            =   1680
         TabIndex        =   16
         Text            =   "Text5"
         Top             =   2280
         Width           =   1215
      End
      Begin VB.TextBox Text4 
         Height          =   270
         Left            =   480
         TabIndex        =   10
         Text            =   "Text4"
         Top             =   1800
         Width           =   2415
      End
      Begin VB.TextBox Text3 
         Height          =   270
         Left            =   480
         TabIndex        =   9
         Text            =   "Text3"
         Top             =   1560
         Width           =   2415
      End
      Begin VB.TextBox Text2 
         Height          =   270
         Left            =   480
         TabIndex        =   8
         Text            =   "Text2"
         Top             =   720
         Width           =   2415
      End
      Begin VB.TextBox Text1 
         Height          =   270
         Left            =   480
         TabIndex        =   7
         Text            =   "Text1"
         Top             =   480
         Width           =   2415
      End
      Begin VB.Label Label7 
         Caption         =   "起点-终点顺向夹角"
         Height          =   255
         Left            =   120
         TabIndex        =   15
         Top             =   2280
         Width           =   3015
      End
      Begin VB.Label Unit 
         Caption         =   "(m)"
         Height          =   255
         Index           =   3
         Left            =   2880
         TabIndex        =   14
         Top             =   1800
         Width           =   255
      End
      Begin VB.Label Unit 
         Caption         =   "(m)"
         Height          =   255
         Index           =   2
         Left            =   2880
         TabIndex        =   13
         Top             =   1560
         Width           =   255
      End
      Begin VB.Label Unit 
         Caption         =   "(m)"
         Height          =   255
         Index           =   1
         Left            =   2880
         TabIndex        =   12
         Top             =   720
         Width           =   255
      End
      Begin VB.Label Unit 
         Caption         =   "(m)"
         Height          =   255
         Index           =   0
         Left            =   2880
         TabIndex        =   11
         Top             =   480
         Width           =   255
      End
      Begin VB.Label Label6 
         Caption         =   "Ep1"
         Height          =   375
         Left            =   120
         TabIndex        =   6
         Top             =   1800
         Width           =   855
      End
      Begin VB.Label Label5 
         Caption         =   "Ap1"
         Height          =   375
         Left            =   120
         TabIndex        =   5
         Top             =   1560
         Width           =   615
      End
      Begin VB.Label Label4 
         Caption         =   "Ep0"
         Height          =   255
         Left            =   120
         TabIndex        =   4
         Top             =   720
         Width           =   495
      End
      Begin VB.Label Label3 
         Caption         =   "Ap0"
         Height          =   255
         Left            =   120
         TabIndex        =   3
         Top             =   480
         Width           =   1335
      End
      Begin VB.Label Label2 
         Caption         =   "目标星球"
         Height          =   375
         Left            =   120
         TabIndex        =   2
         Top             =   1320
         Width           =   1575
      End
      Begin VB.Label Label1 
         Caption         =   "起点星球"
         Height          =   495
         Left            =   120
         TabIndex        =   1
         Top             =   240
         Width           =   3495
      End
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
