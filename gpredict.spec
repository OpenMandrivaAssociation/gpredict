%define name    gpredict
%define version 1.3
%define rel     2

Name:           %{name}
Version:        %{version}
Release:        %{rel}
Summary:        Fast and accurate real-time satellite tracking
Group:          Sciences/Geosciences
License:        GPLv2+
URL:            http://gpredict.oz9aec.net
Source0:         http://sourceforge.net/projects/gpredict/files/Gpredict/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(gtk+)
BuildRequires:  intltool >= 0.21
BuildRequires:  pkgconfig(goocanvas)
       
%description
Gpredict includes the following features:
  * Tracking an infinite number of satellites only limited by the
    physical memory and processing power of the computer.
  * Display the tracking data in lists, maps, polar plots and any
    combination of these.
  * You can have many modules open at the same either in a
    notebook or in their own windows. The module can also run in
    full-screen mode.
  * You can use many ground stations. Ground station coordinates
    can either be entered manually or you can get some appriximate values
    from a list with more than 2000 predefined locations worldwide.
  * Predict upcoming passes for satellites, including passes where a
    satellite may be visible and communication windows
  * Very detailed information about both the real time data and the
    predicted passes.
  * Gpredict can run in real-time, simulated real-time (fast forward and
    backward), and manual time control.
  * Doppler tuning of radios via Hamlib rigctld.
  * Antenna rotator control via Hamlib rotctld.

       
%prep
%setup -q
       
%build
%configure2_5x --enable-coverage
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/%{name}-icon.png
%{_mandir}/man1/gpredict.*


%changelog
* Mon Mar 14 2011 Jani Välimaa <wally@mandriva.org> 1.3-1mdv2011.0
+ Revision: 644702
- new version 1.3
- fix license
- drop unneeded BRs

* Sat Dec 04 2010 Thomas Spuhler <tspuhler@mandriva.org> 1.2-1mdv2011.0
+ Revision: 609560
- removed the dot at the end of the Summary line
- import gpredict

