Summary:	BS2B (Bauer stereophonic-to-binaural DSP) project documentation
Summary(pl.UTF-8):	Dokumentacja projektu BS2B (DSP stereofoniczno-dwuusznego Bauera)
Name:		bs2b-description
Version:	3.0.0
Release:	1
License:	MIT
Group:		Documentation
Source0:	http://downloads.sourceforge.net/bs2b/%{name}-%{version}.tar.gz
# Source0-md5:	e9a05f430cc79a631335a132aa62246a
URL:		http://bs2b.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the BS2B (Bauer stereophonic-to-binaural DSP)
project documentation.

%description -l pl.UTF-8
Ten pakiet zawiera dokumentację projektu BS2B (DSP
stereofoniczno-dwuusznego Bauera).

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html *.png favicon.ico img
