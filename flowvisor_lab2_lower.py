from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
from pox.openflow.of_json import *
from pox.lib.recoco import Timer


log = core.getLogger()
s1_dpid = 0
s2_dpid = 0
s3_dpid = 0
s4_dpid = 0


def _timer_func():
    for connection in core.openflow._connections.values():
        connection.send(of.ofp_stats_request(body=of.ofp_port_stats_request()))
        print "Sent %i port stats request(s)" % (len(core.openflow._connections))


def _handle_portstats_received(event):
    # stats=flow_stats_to_list(event.stats)
    # print "PortStatsReceived from %s: %s" % (dpidToStr(event.connection.dpid), stats)
    for f in event.stats:
        if int(f.port_no) < 65534:
            print "PortNo:", f.port_no, " dpid:", event.connection.dpid


def _handle_ConnectionUp(event):
    global s1_dpid, s2_dpid, s3_dpid, s4_dpid
    print "ConnectionUp: ",
    dpidToStr(event.connection.dpid)
    # remember the connection dpid for switch
    for m in event.connection.features.ports:
        if m.name == "s1-eth2":
            s1_dpid = event.connection.dpid
            print "s1_dpid=", s1_dpid
        elif m.name == "s2-eth1":
            s2_dpid = event.connection.dpid
            print "s2_dpid=", s2_dpid
        elif m.name == "s3-eth1":
            s3_dpid = event.connection.dpid
            print "s3_dpid=", s3_dpid
        elif m.name == "s4-eth2":
            s4_dpid = event.connection.dpid
            print "s4_dpid=", s4_dpid


def _handle_PacketIn(event):
    global s1_dpid, s2_dpid, s3_dpid, s4_dpid
    print "PacketIn: ", dpidToStr(event.connection.dpid)
    if event.connection.dpid == s1_dpid:
        msg = of.ofp_flow_mod()
        msg.priority = 1
        msg.idle_timeout = 0
        msg.hard_timeout = 0
        msg.match.in_port = 4
        msg.actions.append(of.ofp_action_output(port=2))
        event.connection.send(msg)
        msg = of.ofp_flow_mod()
        msg.priority = 1
        msg.idle_timeout = 0
        msg.hard_timeout = 0
        msg.match.in_port = 2
        msg.actions.append(of.ofp_action_output(port=4))
        event.connection.send(msg)
    elif event.connection.dpid == s3_dpid:
        msg = of.ofp_flow_mod()
        msg.priority = 1
        msg.idle_timeout = 0
        msg.hard_timeout = 0
        msg.match.in_port = 1
        msg.actions.append(of.ofp_action_output(port=2))
        event.connection.send(msg)
        msg = of.ofp_flow_mod()
        msg.priority = 1
        msg.idle_timeout = 0
        msg.hard_timeout = 0
        msg.match.in_port = 2
        msg.actions.append(of.ofp_action_output(port=1))
        event.connection.send(msg)
    elif event.connection.dpid == s4_dpid:
        msg = of.ofp_flow_mod()
        msg.priority = 1
        msg.idle_timeout = 0
        msg.hard_timeout = 0
        msg.match.in_port = 2
        msg.actions.append(of.ofp_action_output(port=4))
        event.connection.send(msg)
        msg = of.ofp_flow_mod()
        msg.priority = 1
        msg.idle_timeout = 0
        msg.hard_timeout = 0
        msg.match.in_port = 4
        msg.actions.append(of.ofp_action_output(port=2))
        event.connection.send(msg)


def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    core.openflow.addListenerByName("PortStatsReceived", _handle_portstats_received)
    Timer(5, _timer_func, recurring=True)

