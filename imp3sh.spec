Summary:	Flexible mp3/ogg player with a shell-like interface
Summary(pl):	Elastyczny mp3/ogg player z shell-podobnym interfejsem
Name:		imp3sh
Version:	0.2.4
Release:	1
License:	GPL
Group:		Applications/Sound
Source0: 	http://www.geocities.com/kman_can/%{name}-%{version}.tar.gz
# Source0-md5:	82299c403a3bcb69519c0aefa319c372
URL:		http://www.geocities.com/kman_can/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRequires:	libao-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
imp3sh is an mp3/ogg player with a shell-like interface and over 90
built-in commands and hotkeys. imp3sh is also a terminal shell. imp3sh
uses the Xaudio Asynchronous Library for decoding MP3's and the libogg
and libvorbis libraries.

%description -l pl
imp3sh jest mp3/ogg playerem z shell-podobnym interfejsem, wbudowane
jest w niego ponad 90 poleceñ. imp3sh jest pe³ni funkcjê shella. Do
dzia³ania u¿ywa biblioteki Xaudio Asynchronous do dekodowania MP3,
libogg i libvorbis.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README TODO
%attr(755,root,root) %{_bindir}/*
