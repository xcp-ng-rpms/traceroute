Summary: Traces the route taken by packets over an IPv4/IPv6 network
Name: traceroute
Version: 2.1.5
Release: 1%{?dist}
Group: Applications/Internet
License: GPLv2+
URL:  http://traceroute.sourceforge.net
Source0: http://dl.sourceforge.net/traceroute/traceroute-%{version}.tar.gz

BuildRequires: gcc

%description
The traceroute utility displays the route used by IP packets on their
way to a specified network (or Internet) host.  Traceroute displays
the IP number and host name (if possible) of the machines along the
route taken by the packets.  Traceroute is used as a network debugging
tool.  If you're having network connectivity problems, traceroute will
show you where the trouble is coming from along the route.

Install traceroute if you need a tool for diagnosing network connectivity
problems.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=""

%install
install -d $RPM_BUILD_ROOT%{_bindir}
install -m755 traceroute/traceroute $RPM_BUILD_ROOT%{_bindir}
ln -sr $RPM_BUILD_ROOT/bin/traceroute $RPM_BUILD_ROOT%{_bindir}/traceroute6

install -d $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m644 traceroute/traceroute.8 $RPM_BUILD_ROOT%{_mandir}/man8
ln -s traceroute.8 $RPM_BUILD_ROOT%{_mandir}/man8/traceroute6.8

%files
%doc COPYING README TODO CREDITS
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Fri Apr 26 2024 Thierry Escande <thierry.escande@vates.tech> - 2.1.5-1
- Imported from upstream version 2.1.5
