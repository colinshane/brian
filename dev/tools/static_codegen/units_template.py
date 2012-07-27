'''
THIS FILE IS AUTOMATICALLY GENERATED BY A STATIC CODE GENERATION TOOL
DO NOT EDIT BY HAND

Instead edit the template in the SVN:

    /dec/tools/static_codegen/units_template.py
'''
from fundamentalunits import *
from fundamentalunits import standard_unit_register, additional_unit_register
import fundamentalunits
from brian_unit_prefs import bup

fundamentalunits.automatically_register_units = False

#### FUNDAMENTAL UNITS
metre = Unit.create(Dimension(m=1), "metre", "m")
meter = Unit.create(Dimension(m=1), "meter", "m")
kilogram = Unit.create(Dimension(kg=1), "kilogram", "kg")
gram = Unit.create_scaled_unit(kilogram, "m")
gram.set_name('gram')
gram.set_display_name('g')
gramme = Unit.create_scaled_unit(kilogram, "m")
gramme.set_name('gramme')
gramme.set_display_name('g')
second = Unit.create(Dimension(s=1), "second", "s")
amp = Unit.create(Dimension(A=1), "amp", "A")
kelvin = Unit.create(Dimension(K=1), "kelvin", "K")
mole = Unit.create(Dimension(mol=1), "mole", "mol")
candle = Unit.create(Dimension(candle=1), "candle", "cd")
fundamental_units = [ metre, meter, gram, second, amp, kelvin, mole, candle ]

{derived}

{all}

{definitions}

{base_units}
{scaled_units}
{powered_units}
{additional_units}
{all_units}

fundamentalunits.automatically_register_units = True

map(standard_unit_register.add, base_units + scaled_units + powered_units)
map(additional_unit_register.add, additional_units)

if __name__ == "__main__":
    from numpy import *
    # shorthand function used for example code below
    def pE(vname, str):
        uname = vname
        if vname == "": uname = "temp"
        exec(uname + "=" + str)
        if vname != "": print vname, "=",
        print str,
        if locals()[uname] != None:
            print '=', locals()[uname]
        else:
            print
        return locals()[uname]

    V = pE("V", "3 * volt")
    I = pE("I", "2 * amp")
    a = pE("a", "array([1,2,3])")
    print
    R = pE("R", "V/I")
    pE("", "I*R")
    print
    pE("", "a*V")
    pE("", "V*a")
    pE("", "a+V")
    print
    pE("", "1000*metre")
    pE("", "1000*mmetre")
    print
    pE("", "(2*volt).in_unit(mvolt)")
    pE("", "(2*volt)/mvolt")
    print "(2*volt).in_unit(amp) =",
    try:
        print (2 * volt).in_unit(amp)
    except DimensionMismatchError, i:
        print "DimensionMismatchError:", i
    print
    pE("", "have_same_dimensions(1*volt,1*amp*ohm)")
    pE("", "have_same_dimensions(1*volt*second,1*amp*ohm)")
    print
    pE("", "(ufarad/nmetre)**2")
    print
    pE("", "2.0*farad/metre**2")
    pE("", "register_new_unit(pfarad / mmetre**2)")
    pE("", "2.0*farad/metre**2")

    print
    print "Some decorator examples (see code):"
    print

    @check_units(I=amp, R=ohm, wibble=metre, result=volt)
    def getvoltage(I, R, *args, **k):
        return I * R

    try:
        print getvoltage(1 * amp, 2 * ohm, 20)
        print getvoltage(R=2 * ohm, I=1 * amp, wibble=7 * mmetre)
        print getvoltage(1 * amp, 2 * ohm * metre)
    except DimensionMismatchError, inst:
        print "DME:", inst

    print
    pE("", "get_unit(3*msecond)")
