%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		khangman
Summary:	khangman
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	4fc3dc566d2869f93ce561f88644bb87
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel >= 5.11.1
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= 18.12.0
BuildRequires:	ka5-libkeduvocdocument-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcompletion-devel >= 5.15.0
BuildRequires:	kf5-kconfig-devel >= 5.15.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.15.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.15.0
BuildRequires:	kf5-kcrash-devel >= 5.15.0
BuildRequires:	kf5-kdeclarative-devel >= 5.15.0
BuildRequires:	kf5-kdoctools-devel >= 5.15.0
BuildRequires:	kf5-ki18n-devel >= 5.15.0
BuildRequires:	kf5-kio-devel >= 5.15.0
BuildRequires:	kf5-knewstuff-devel >= 5.15.0
BuildRequires:	kf5-knotifications-devel >= 5.15.0
BuildRequires:	kf5-kxmlgui-devel >= 5.15.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KHangMan is the classical hangman game. The child should guess a word
letter by letter. At each miss, the picture of a hangman appears.
After 10 tries, if the word is not guessed, the game is over and the
answer is displayed.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/khangman.knsrc
%attr(755,root,root) %{_bindir}/khangman
%{_desktopdir}/org.kde.khangman.desktop
%{_datadir}/config.kcfg/khangman.kcfg
%{_iconsdir}/hicolor/128x128/apps/khangman.png
%{_iconsdir}/hicolor/16x16/apps/khangman.png
%{_iconsdir}/hicolor/22x22/apps/khangman.png
%{_iconsdir}/hicolor/32x32/apps/khangman.png
%{_iconsdir}/hicolor/48x48/apps/khangman.png
%{_iconsdir}/hicolor/64x64/apps/khangman.png
%{_iconsdir}/hicolor/scalable/apps/khangman.svgz
%{_datadir}/khangman
%lang(ca) %{_mandir}/ca/man6/khangman.6*
%lang(de) %{_mandir}/de/man6/khangman.6*
%lang(es) %{_mandir}/es/man6/khangman.6*
%lang(et) %{_mandir}/et/man6/khangman.6*
%lang(it) %{_mandir}/it/man6/khangman.6*
%lang(C) %{_mandir}/man6/khangman.6*
%lang(nl) %{_mandir}/nl/man6/khangman.6*
%lang(pt) %{_mandir}/pt/man6/khangman.6*
%lang(pt_BR) %{_mandir}/pt_BR/man6/khangman.6*
%lang(sv) %{_mandir}/sv/man6/khangman.6*
%lang(uk) %{_mandir}/uk/man6/khangman.6*
%{_datadir}/metainfo/org.kde.khangman.appdata.xml
