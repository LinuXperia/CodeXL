import os
import sys
workspace = os.path.dirname(os.path.realpath(__file__))
tempfolder = workspace+"\\TestTemp"
os.environ ["TEMP"] = tempfolder
currenttemp =  os.environ.get ("TEMP")
print ("Temp folder set to - "+currenttemp)
print ("")
os.chdir(workspace )

# Run CodeXL Debugger test
os.system( 'CodeXLGpuDebuggingTest.exe CodeXL_GPU_Debugging_Tests_x64.xml --gtest_output=xml:CodeXL_Results_GPU_Debugging_Test_x64.xml"' )

# Run CodeXL GPU Profiling test
os.system( '"CodeXL_GpuProfiler_TestCLGetKernelInfoAMD-x64.exe --gtest_output=xml:CodeXL_Results_GPU_Profiling_GetKernelInfo-x64.xml"' )
os.system( '"CodeXL_GpuProfiler_TestCLPMCAPI-x64.exe --gtest_output=xml:CodeXL_Results_GPU_Profiling_PMCAPI-x64.xml"' )
