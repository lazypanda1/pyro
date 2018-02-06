from __future__ import absolute_import, division, print_function

import torch

from .clipped_adam import ClippedAdam as pt_ClippedAdam
from .optim import PyroOptim


def Adam(optim_args):
    """
    A wrapper for torch.optim.Adam
    """
    assert (optim_args['betas'][0] >= 0.0 and optim_args['betas'][0] < 1.0 \
        if isinstance(optim_args, dict) and 'betas' in optim_args.keys() else True), "Invalid beta parameter at index 0: %f" % optim_args['betas'][0]
    assert (optim_args['betas'][1] >= 0.0 and optim_args['betas'][1] < 1.0 \
        if isinstance(optim_args, dict) and 'betas' in optim_args.keys() else True), "Invalid beta parameter at index 1: %f" % optim_args['betas'][1]
    return PyroOptim(torch.optim.Adam, optim_args)


def Adadelta(optim_args):
    """
    A wrapper for torch.optim.Adadelta
    """
    return PyroOptim(torch.optim.Adadelta, optim_args)


def Adagrad(optim_args):
    """
    A wrapper for torch.optim.Adagrad
    """
    return PyroOptim(torch.optim.Adagrad, optim_args)


def Adamax(optim_args):
    """
    A wrapper for torch.optim.Adamax
    """
    return PyroOptim(torch.optim.Adamax, optim_args)


def ASGD(optim_args):
    """
    A wrapper for torch.optim.ASGD
    """
    return PyroOptim(torch.optim.ASGD, optim_args)


def RMSprop(optim_args):
    """
    A wrapper for torch.optim.RMSprop
    """
    return PyroOptim(torch.optim.RMSprop, optim_args)


def Rprop(optim_args):
    """
    A wrapper for torch.optim.Rprop
    """
    return PyroOptim(torch.optim.Rprop, optim_args)


def SGD(optim_args):
    """
    A wrapper for torch.optim.SGD
    """
    return PyroOptim(torch.optim.SGD, optim_args)


def ClippedAdam(optim_args):
    """
    A wrapper for a modification of the Adam optimization algorithm that supports gradient clipping
    """
    return PyroOptim(pt_ClippedAdam, optim_args)
