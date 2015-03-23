import numpy as np

def model(t, p):
    """
    This is the Analytic Flare Model from the flare-morphology paper
    Please reference Davenport (2014) http://arxiv.org/abs/1411.3723

    Parameters
    ----------
    t : 1-d array
        The time array to evaluate the flare over
    p : 1-d array
        p == [tpeak, fwhm (units of time), amplitude (units of flux)] x N

    Returns
    -------
    flare : 1-d array
        The fluxes of the flare model
    """
    _fr = [1.00000, 1.94053, -0.175084, -2.24588, -1.12498]
    _fd = [0.689008, -1.60053, 0.302963, -0.278318]

    Nflare = np.floor( (len(p)/3.0) )

    flare = np.zeros_like(t)
    # compute the flare model for each flare
    for i in range(Nflare):
        outm = (((_fr[0]+#                                ; 0th order
                  _fr[1]*((t-p[0+i*3])/p[1+i*3])+#        ; 1st order
                  _fr[2]*((t-p[0+i*3])/p[1+i*3])^2.+#     ; 2nd order
                  _fr[3]*((t-p[0+i*3])/p[1+i*3])^3.+#     ; 3rd order
                  _fr[4]*((t-p[0+i*3])/p[1+i*3])^4. )*#   ; 4th order
                 (t le p[0+i*3] and (t-p[0+i*3])/p[1+i*3] gt -1.) + # ; rise  mask
                 ( _fd[0]*exp( ((t-p[0+i*3])/p[1+i*3])*_fd[1] ) + #     ; first exp
                   _fd[2]*exp( ((t-p[0+i*3])/p[1+i*3])*_fd[3] ) ) * #   ; second exp
                 (t gt p[0+i*3])) *#                                 ; decay  mask
                P[2+i*3])  #                                            ; amplitude
        
        flare = flare + outm
        
    return flare
