# 
# Do not Edit! Generated by:
# spectacle version 0.18
# 
# >> macros
#%define wantmeegopanel 0
#%define all_x86 i386 i586 i686 %{ix86}
#%define all_arm %{arm}
# << macros
%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}

Name:       harbour-meecast
Summary:    Weather forecast application for SailfishOS
Version:    0.8.16
Release:    1
Group:      Utility
License:    GPLv2.1
URL:        https://github.com/Meecast/meecast 
Source0:    %{name}-%{version}.tar.bz2
#Temporary
#Requires:       libmeegotouch-devel
BuildRequires:  pkgconfig(sailfishapp)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(qdeclarative5-boostable)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(sqlite3)
#BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libxml-2.0)
#BuildRequires:  libxml2-devel
BuildRequires:  gettext
#BuildRequires:  libqt-devel
BuildRequires: qt5-qtpositioning-devel
#Requires:      qt5-qtpositioning 
#Requires:      sailfishsilica-qt5
#Requires:      qt5-qtdeclarative-import-models2 
#Requires:      zlib 

%description
MeeCast - multiplatform highly customizable open source weather forecast client based on OMWeather code



%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
#export PATH=/usr/lib/qt4/bin:$PATH
%qtc_qmake5
%qtc_make %{?_smp_mflags}
#make
# << build pre


# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
%qmake5_install
#make INSTALL_ROOT=%{buildroot} install
#rm %{buildroot}/opt/com.meecast.omweather/lib/libomweather-core.a
# << install post
desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop


%files
%defattr(-,root,root,-)
/usr/share/applications/harbour-meecast.desktop
/usr/bin/harbour-meecast
/usr/share/harbour-meecast
#/usr/share/iconsets
/usr/share/icons/hicolor/86x86/apps
#/opt/com.meecast.omweather/share

%changelog
* Wed Mar 26 2014 Vlad Vasilyeu <vasvlad@gmail.com> 0.8.16.1
  * Fixed segmentation fault 
  * Fixed problem with translations
  * Fixed problem with logo on cover page
  * Fixed centering problem of the graphics on the details page
  * Increased icon size on CoverPage
  * Reordered items in Main PullMenu

* Wed Mar 26 2014 Vlad Vasilyeu <vasvlad@gmail.com> 0.8.15.1
  * Updated Denmark for openstreetmap.org 
  * Disabled menu item "Adjust GPS station"
  * Fixed problem with crashing application with foreca.com data
  * Changed order of items in PullMenu
  * Fixed font size in station name on Cover Page
  * Fixed problem with size of map image
  * Updated Catalan, Czech, Finnish, Norwegian, Serbian, Slovenian, Spanish,
    Turkish, Germany translations

* Sun Feb 23 2014 Vlad Vasilyeu <vasvlad@gmail.com> 0.8.14.1
  * Fixed problem with downloading

* Sat Feb 22 2014 Vlad Vasilyeu <vasvlad@gmail.com> 0.8.13.1
  * Fixed problem on Cover page

* Sat Feb 22 2014 Vlad Vasilyeu <vasvlad@gmail.com> 0.8.12.1
  * Fixed problem on Cover page

* Sat Feb 22 2014 Vlad Vasilyeu <vasvlad@gmail.com> 0.8.11.1
  * Polished Cover page
  * Disable unused configuration files 

* Wed Feb 18 2014 Vlad Vasilyeu <vasvlad@gmail.com> 0.8.10.1
  * Adapted for Harbour (Jolla store)
  * Disabled GPS-station

* Sat Feb 15 2014 Vlad Vasilyeu <vasvlad@gmail.com> 0.8.9.1
  * Updated Finnish, Norwegian, Arabic, Serbian, Turkish, Dutch, Hungarian translations
  * Added Slovenian and Czech translations
  * Fixed memory leaks
  * Fixed problem with yr.no database for Belarus
  * Added icon and descripion string for openweathermap.org source

* Sun Feb 02 2014 Vlad Vasilyeu <vasvlad@gmail.com> 0.8.8.1
  * Fixed problem with long text in last update string
  * Added possibility to switch off 'Last update' on Cover Page
  * Fixed problem in About Page 
  * Redesigned wind information on Cover Page 
  * Updated Norwegian, Arabic, Serbian, Turkish, Dutch, Hungarian translations
  * Added Slovenian and Czech translations
* Tue Jan 26 2014  Vlad Vasilyeu <vasvlad@gmail.com> 0.8.7.1
  * Added Wind speed and Wind direction to Cover Page
  * Added text 'Now' to Cover Page
  * Polished Cover Page
* Tue Jan 23 2014  Vlad Vasilyeu <vasvlad@gmail.com> 0.8.6.1
  * Removed button refresh from main form and add Item menu 'Update' to pulley menu 
  * Redesigned form for delete location
  * Fixed problem with transparency Cover window and font size on Cover Window
  * Added last update information on Cover Page
  * Added new icons from Stephan Beyerle (Thank you very much Stephan)
  * Added background Image to Cover (Thank you very much Stephan again)
* Sun Jan 19 2014  Vlad Vasilyeu <vasvlad@gmail.com> 0.8.5
  * Fixed various small problems
  * Fixed problem with size of font in CoverPage
  * Fixed problem with scroll down for hours in FullWeather page
  * Added possibility to refresh weather forecast using the CoverPage
  * Fixed problem with open many applications(MeeCast) when you click the icon 
* Sat Jan 18 2014  Vlad Vasilyeu <vasvlad@gmail.com> 0.8.4.2
  * Fixed problem with refreshing weather forecast
* Fri Jan 17 2014  Vlad Vasilyeu <vasvlad@gmail.com> 0.8.4.1
  * First release SailfishOS
# << files


