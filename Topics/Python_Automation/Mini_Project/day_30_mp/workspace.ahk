; -------------------------------------------------------------
; Willy’s Dual-Monitor + Dual-Desktop Automation Script
; -------------------------------------------------------------
; Requirements: AutoHotkey v1.1+, Chrome, VS Code, Spotify
; -------------------------------------------------------------

#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%
#SingleInstance Force

; === PATHS ===
chromePath := "C:\Program Files\Google\Chrome\Application\chrome.exe"
vscodePath := "C:\Users\ADMIN\AppData\Local\Programs\Microsoft VS Code\Code.exe"


; === MONITOR SETUP ===
; Laptop = left (0,0 → 1920x1080)
; Monitor = right (1920,0 → 3840x1080)

; -------------------------------------------------------------
; === DESKTOP 1: ChatGPT (laptop) + VS Code (monitor)
; -------------------------------------------------------------
; Switch to Desktop 1
Send, ^#{Left}
Sleep, 800

; --- Open ChatGPT on laptop ---
Run, %chromePath% "https://chat.openai.com"
WinWait, ahk_exe chrome.exe
Sleep, 2500
WinMove, ahk_exe chrome.exe, , 0, 0, 1920, 1080
Sleep, 300

; --- Open VS Code on monitor ---
Run, %vscodePath%
WinWait, ahk_exe Code.exe, , 15  ; wait up to 15 seconds
Sleep, 2000
WinActivate, ahk_exe Code.exe
WinMove, ahk_exe Code.exe, , 1920, 0, 1920, 1080
Sleep, 500

; -------------------------------------------------------------
; === DESKTOP 2: Timer (laptop) + Spotify (monitor)
; -------------------------------------------------------------
; Switch to Desktop 2
Send, ^#{Right}
Sleep, 800

; --- Open vClock Pomodoro Timer (50 mins) on laptop ---
Run, %chromePath% "https://vclock.com/timer/#countdown=00:50:00&date=2025-11-03T16:11:50&sound=bells&loop=1"
WinWait, ahk_exe chrome.exe
Sleep, 3000
WinMaximize, ahk_exe chrome.exe
Sleep, 300

; --- Open Spotify on monitor ---
Run, spotify.exe
WinWait, ahk_exe Spotify.exe, , 15  ; wait up to 15 seconds
Sleep, 2500
WinMove, ahk_exe Spotify.exe, , 1920, 0, 1920, 1080
Sleep, 300

; -------------------------------------------------------------
MsgBox, All apps launched and arranged successfully!
ExitApp
