%define name    gpredict
%define version 1.2
%define rel     1

Name:           %{name}
Version:        %{version}
Release:        %mkrel %{rel}
Summary:        Fast and accurate real-time satellite tracking
Group:          Sciences/Geosciences
License:        GPLv2
URL:            http://gpredict.oz9aec.net
Source:         http://sourceforge.net/projects/gpredict/files/Gpredict/1.2/%{name}-%{version}.tar.gz
BuildRequires:  hamlib
BuildRequires:  libncurses-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libcurl-devel
BuildRequires:  gtk+-devel
BuildRequires:  intltool >= 0.21
BuildRequires:  goocanvas-devel
       
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
%make LIBS=-lm

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}
%{_mandir}/man1/gpredict.*
