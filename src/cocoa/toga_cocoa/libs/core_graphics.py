##########################################################################
# System/Library/Frameworks/CoreGraphics.framework
##########################################################################
from ctypes import *
from ctypes import util

from rubicon.objc.types import register_preferred_encoding
from rubicon.objc import *


######################################################################
core_graphics = cdll.LoadLibrary(util.find_library('CoreGraphics'))
######################################################################

######################################################################
# CGContext.h

CGPathDrawingMode = c_uint32

core_graphics.CGContextAddArc.restype = c_void_p
core_graphics.CGContextAddArc.argtypes = [c_void_p, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, c_int]
core_graphics.CGContextAddCurveToPoint.restype = c_void_p
core_graphics.CGContextAddCurveToPoint.argtypes = [c_void_p, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat]
core_graphics.CGContextAddLineToPoint.restype = c_void_p
core_graphics.CGContextAddLineToPoint.argtypes = [c_void_p, CGFloat, CGFloat]
core_graphics.CGContextAddQuadCurveToPoint.restype = c_void_p
core_graphics.CGContextAddQuadCurveToPoint.argtypes = [c_void_p, CGFloat, CGFloat, CGFloat, CGFloat]
core_graphics.CGContextAddRect.restype = c_void_p
core_graphics.CGContextAddRect.argtypes = [c_void_p, CGRect]
core_graphics.CGContextBeginPath.restype = c_void_p
core_graphics.CGContextBeginPath.argtypes = [c_void_p]
core_graphics.CGContextClosePath.restype = c_void_p
core_graphics.CGContextClosePath.argtypes = [c_void_p]
core_graphics.CGContextDrawPath.restype = c_void_p
core_graphics.CGContextDrawPath.argtypes = [c_void_p, CGPathDrawingMode]
core_graphics.CGContextMoveToPoint.restype = c_void_p
core_graphics.CGContextMoveToPoint.argtypes = [c_void_p, CGFloat, CGFloat]
core_graphics.CGContextRestoreGState.restype = c_void_p
core_graphics.CGContextRestoreGState.argtypes = [c_void_p]
core_graphics.CGContextRotateCTM.restype = c_void_p
core_graphics.CGContextRotateCTM.argtypes = [c_void_p, CGFloat]
core_graphics.CGContextSaveGState.restype = c_void_p
core_graphics.CGContextSaveGState.argtypes = [c_void_p]
core_graphics.CGContextScaleCTM.restype = c_void_p
core_graphics.CGContextScaleCTM.argtypes = [c_void_p, CGFloat, CGFloat]
core_graphics.CGContextSetLineWidth.restype = c_void_p
core_graphics.CGContextSetLineWidth.argtypes = [c_void_p, CGFloat]
core_graphics.CGContextSetRGBFillColor.restype = c_void_p
core_graphics.CGContextSetRGBFillColor.argtypes = [c_void_p, CGFloat, CGFloat, CGFloat, CGFloat]
core_graphics.CGContextSetRGBStrokeColor.restype = c_void_p
core_graphics.CGContextSetRGBStrokeColor.argtypes = [c_void_p, CGFloat, CGFloat, CGFloat, CGFloat]
core_graphics.CGContextTranslateCTM.restype = c_void_p
core_graphics.CGContextTranslateCTM.argtypes = [c_void_p, CGFloat, CGFloat]

######################################################################
# CGEvent.h
CGEventRef = c_void_p
register_preferred_encoding(b'^{__CGEvent=}', CGEventRef)

CGEventSourceRef = c_void_p
register_preferred_encoding(b'^{__CGEventSource=}', CGEventSourceRef)

CGScrollEventUnit = c_uint32

core_graphics.CGEventCreateScrollWheelEvent.argtypes = [CGEventSourceRef, CGScrollEventUnit, c_uint32, c_int32, c_int32]
core_graphics.CGEventCreateScrollWheelEvent.restype = CGEventRef

######################################################################
# CGEventTypes.h
kCGScrollEventUnitPixel = 0
kCGScrollEventUnitLine = 1

######################################################################
# CGImage.h
kCGImageAlphaNone = 0
kCGImageAlphaPremultipliedLast = 1
kCGImageAlphaPremultipliedFirst = 2
kCGImageAlphaLast = 3
kCGImageAlphaFirst = 4
kCGImageAlphaNoneSkipLast = 5
kCGImageAlphaNoneSkipFirst = 6
kCGImageAlphaOnly = 7

kCGImageAlphaPremultipliedLast = 1

kCGBitmapAlphaInfoMask = 0x1F
kCGBitmapFloatComponents = 1 << 8

kCGBitmapByteOrderMask = 0x7000
kCGBitmapByteOrderDefault = 0 << 12
kCGBitmapByteOrder16Little = 1 << 12
kCGBitmapByteOrder32Little = 2 << 12
kCGBitmapByteOrder16Big = 3 << 12
kCGBitmapByteOrder32Big = 4 << 12
