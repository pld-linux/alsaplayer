Summary:	Alsaplayer - CD/FLAC/MOD/MP3/OGG/WAV player
Summary(pl):	Alsaplayer - odtwarzacz CD/FLAC/MOD/MP3/OGG/WAV
Name:		alsaplayer
Version:	0.99.75
Release:	0.4
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.alsa-project.org/pub/people/andy/%{name}-%{version}.tar.bz2
# Source0-md5:	353b57058e05aa5f0c01f93fc049c650
Source1:	%{name}.desktop
Patch0:		%{name}-docs.patch
Patch1:		%{name}-gcc33.patch
URL:		http://www.alsaplayer.org/
BuildRequires:	OpenGL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	flac-devel
BuildRequires:	gtk+-devel
BuildRequires:	id3lib-devel
BuildRequires:	jack-audio-connection-kit-devel >= 0.69.1
BuildRequires:	libmikmod-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	mad-devel
BuildRequires:	nas-devel
BuildRequires:	xosd-devel
Requires(post):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_pkglibdir	%{_libdir}/%{name}

%description
AlsaPlayer is a new type of PCM player. It is heavily multi-threaded
and tries to exercise the ALSA library and driver quite a bit.
Features include:

Input addons:
 - MP2 and MP3 support
 - Ogg Vorbis support (subpackage)
 - WAV support, 8-, 16-bit, mono, stereo, any sample rate
 - CDDA support, CD Digital Audio playback! and thus USB ready :)
 - Also plays files mapped by audiofs (CDDA)
 - MAD MPEG audio
 - Module support (mikmod) (subpcakage)
 - FLAC support

Output addons:
 - ALSA. Best supported of course :) (subpackage)
 - OSS. Kernel native sound drivers
 - Sparc. UltraSparc sound drivers
 - SGI. SGI audio library driver
 - ESD. Enlightened sound daemon support (subpackage)
 - NAS. Network Audio System (subpakcage)
 - low latency JACK output
 - null :-)

Visual scopes:
 - Stereoscope
 - Monoscope
 - Levelmeter
 - Spacescope
 - FFTscope
 - FFTscope II
 - Spectrum GL

General features:
 - Full speed (pitch) control, positive *and* negative! (First Linux
   player that does this!! MP3's and CD's do varispeed :)
 - Queue (playlist) support
 - Concurrent visual scopes (open as many as you want)
 - Multi-threaded design for efficient/skip free playback (RT)
 - GUI Interface based on gtk+
 - NOGUI operation for shell script usage
 - On-screen-display based on xosd
 - Plug-in core architecture
 - Low latency mode, as low as 5ms when scheduled RT
 - Effects stream
 - Software based volume/pan control
 - Accurate scope/audio syncing using ALSA features

%description -l pl
AlsaPlayer to nowy rodzaj odtwarzacza PCM. Jest wielow�tkowy i pr�buje
solidnie prze�wiczy� sterowniki i bibliotek� ALSA. Jego cechy to:

Wej�cie:
 - obs�uga MP2 i MP3
 - obs�uga Ogg Vorbis (w podpakiecie)
 - obs�uga WAV, 8 i 16-bitowych, mono, stereo o dowolnej cz�stotliwo�ci
 - obs�uga CD Digital Audio
 - odtwarzanie plik�w podmapowanych przez audiofs (CDDA)
 - obs�uga MAD - MPEG Audio
 - obs�uga modu��w (mikmod) (w podpakiecie)
 - obs�ug bezstratnej kompresji d�wi�ku FLAC

Wyj�cie:
 - OSS - natywne sterowniki z j�dra
 - ALSA - oczywi�cie najlepiej obs�ugiwana :) (w podpakiecie)
 - Sparc - sterowniki d�wi�ku dla UltraSparca
 - SGI - biblioteka sterownik�w d�wi�ku SGI
 - ESD - obs�uga O�wieconego demona d�wi�ku (w podpakiecie)
 - NAS - Sieciowego Systemu Audio (w podpakiecie)
 - JACK - zestaw po��cze� d�wi�ku o ma�ych op�nieniach (w podpakiecie)
 - null :-)

Wizualizacja:
 - Stereoskop
 - Monoskop
 - Wska�nik poziomu d�wi�ku
 - Wska�niki oparte o analiz� FFT
 - analizator spektrum sygna�u w oparciu o OpenGL

Og�lne cechy:
 - Kontrola szybko�ci (w obie strony)
 - obs�uga kolejki (playlisty)
 - obs�uga wielu wska�nik�w naraz
 - wielow�tkowo��
 - interfejs graficzny bazuj�cy na gtk+
 - operacje bez GUI na potrzeby skrypt�w
 - tryb Informacje-na-ekranie oparty o xosd
 - architektura wtyczek
 - tryb "czasu rzeczywistego" daj�cy op�nienia rz�du 5ms
 - programowa kontrola g�o�no�ci i balansu
 - synchronizacja d�wi�ku i wska�nik�w przy u�yciu mo�liwo�ci ALSA

%package daemon
Summary:	Deamon interface for Alsaplayer
Summary(pl):	Interfejs demona alsaplayera
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description daemon
Deamon interface for Alsaplayer.

%description daemon -l pl
Interfejs demona alsaplayera.

%package input-audiofile
Summary:	Alsaplayer plugin for playing wave audio formats using audiofile
Summary(pl):	Wtyczka alsaplayera do odtwarzania plik�w audio typu wave przy u�yciu audiofile
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description input-audiofile
Alsaplayer plugin for playing wave audio formats (like AIFF, AIFC,
WAVE, ...) using audiofile library.

%description input-audiofile -l pl
Wtyczka alsaplayera do odtwarzania plik�w audio typu wave (AIFF,
AIFC, WAVE, ...) przy u�yciu biblioteki audiofile.

%package input-flac
Summary:	Alsaplayer plugin for playing FLAC files
Summary(pl):	Wtyczka alsaplayera do odtwarzania plik�w FLAC
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description input-flac
Alsaplayer plugin for playing FLAC files.

%description input-flac -l pl
Wtyczka alsaplayera do odtwarzania plik�w FLAC.

%package input-mad
Summary:	Alsaplayer plugin for playing MP3 files using MAD
Summary(pl):	Wtyczka alsaplayera do odtwarzania plik�w MP3 przy pomocy MAD
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description input-mad
Alsaplayer plugin for playing MP3 files using MAD.

%description input-mad -l pl
Wtyczka alsaplayera do odtwarzania plik�w MP3 przy pomocy MAD.

%package input-mikmod
Summary:	Alsaplayer plugin for playing mod files
Summary(pl):	Wtyczka alsaplayera do odtwarzania plik�w mod
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description input-mikmod
Alsaplayer plugin for playing mod files.

%description input-mikmod -l pl
Wtyczka alsaplayera do odtwarzania plik�w mod.

%package input-sndfile
Summary:	Alsaplayer plugin for playing wave audio formats using libsndfile
Summary(pl):	Wtyczka alsaplayera do odtwarzania plik�w audio typu wave przy u�yciu libsndfile
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description input-sndfile
Alsaplayer plugin for playing wave audio formats (like AIFF, AIFC,
WAVE, ...) using libsndfile library.

%description input-sndfile -l pl
Wtyczka do alsaplayera do odtwarzania plik�w audio typu wave (AIFF,
AIFC, WAVE, ...) przy u�yciu biblioteki libsndfile.

%package input-vorbis
Summary:	Alsaplayer plugin for playing ogg/vorbis files
Summary(pl):	Wtyczka alsaplayera do odtwarzania plik�w ogg/vorbis
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description input-vorbis
Alsaplayer plugin for playing ogg/vorbis files.

%description input-vorbis -l pl
Wtyczka alsaplayera do odtwarzania plik�w ogg/vorbis.

%package interface-gtk
Summary:	GTK+ interface for Alsaplayer
Summary(pl):	Interfejs GTK+ alsaplayera
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}

%description interface-gtk
GTK+ interface for Alsaplayer.

%description interface-gtk -l pl
Interfejs GTK+ alsaplayera.

%package interface-text
Summary:	Text interface for Alsaplayer
Summary(pl):	Interfejs tekstowy alsaplayera
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description interface-text
Text interface for Alsaplayer.

%description interface-text -l pl
Interfejs tekstowy alsaplayera.

%package interface-xosd
Summary:	xosd interface for Alsaplayer
Summary(pl):	Interfejs xosd alsaplayera
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}

%description interface-xosd
xosd interface for Alsaplayer.

%description interface-xosd -l pl
Interfejs xosd alsaplayera.

%package output-alsa
Summary:	Alsaplayer plugin for playing through alsa drivers
Summary(pl):	Wtyczka alsaplayera do odtwarzania przez sterowniki alsa
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description output-alsa
Alsaplayer plugin for playing sound through alsa drivers.

%description output-alsa -l pl
Wtyczka alsaplayera do odtwarzania d�wi�ku przez sterowniki alsa.

%package output-esound
Summary:	Alsaplayer plugin for playing through esound daemon
Summary(pl):	Wtyczka alsaplayera do odtwarzania przez demona esound
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description output-esound
Alsaplayer plugin for playing sound through esound daemon.

%description output-esound -l pl
Wtyczka alsaplayera do odtwarzania d�wi�ku przez demona esound.

%package output-nas
Summary:	Alsaplayer plugin for playing through NAS daemon
Summary(pl):	Wtyczka do alsaplayera do odtwarzania przez demona NAS
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description output-nas
Alsaplayer plugin for playing sound through NAS (network audio system)
daemon.

%description output-nas -l pl
Wtyczka alsaplayera do odtwarzania d�wi�ku przez demona NAS (network
audio system).

%package output-jack
Summary:	Alsaplayer plugin for playing sound through JACK
Summary(pl):	Wtyczka alsaplayera do odtwarzania d�wi�ku przez JACK
Group:		Applications/Sound
Requires:	%{name} = %{version}

%description output-jack
Alsaplayer plugin for sound through JACK system.

%description output-jack -l pl
Wtyczka alsaplayera do odtwarzania d�wi�ku przez system JACK.

%package scopes-gtk
Summary:	Alsaplayer plugins for visualization
Summary(pl):	Wtyczki alsaplayera do wizualizacji
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description scopes-gtk
Alsaplayer plugins for visualization.

%description scopes-gtk -l pl
Wtyczki do alsaplayera do wizualizacji.

%package scopes-opengl
Summary:	Alsaplayer plugin for visualization using OpenGL
Summary(pl):	Wtyczka alsaplayera do wizualizacji z u�yciem OpenGL
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}
Requires:	OpenGL

%description scopes-opengl
Alsaplayer plugin for visualization using OpenGL.

%description scopes-opengl -l pl
Wtyczka do alsaplayera do wizualizacji z u�yciem OpenGL.

%package devel
Summary:	Alsaplayer header files
Summary(pl):	Pliki nag��wkowe Alsaplayera
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for Alsaplayer library.

%description devel -l pl
Pliki nag��wkowe biblioteki Alsaplayera.

%package static
Summary:	Alsaplayer static library
Summary(pl):	Biblioteka statyczna Alsaplayera
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Alsaplayer static library.

%description static -l pl
Biblioteka statyczna Alsaplayera.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS=" -I/usr/X11R6/include"
LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib"
export CPPFLAGS LDFLAGS
%configure \
	--enable-alsa \
	--enable-audiofile \
	--enable-esd \
	--enable-flac \
	--enable-gtk \
	--enable-jack \
	--enable-mikmod \
	--enable-nas \
	--enable-oggflac \
	--enable-oggvorbis \
	--enable-opengl \
	--enable-oss \
	--enable-static \
%ifarch sparc
	--enable-sparc
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

rm -f $RPM_BUILD_ROOT%{_pkglibdir}/input/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_pkglibdir}/interface/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_pkglibdir}/output/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_pkglibdir}/reader/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_pkglibdir}/scopes/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_bindir}/alsaplayer
%attr(755,root,root) %{_libdir}/libalsaplayer.so.0.0.2
%dir %{_pkglibdir}
%dir %{_pkglibdir}/input
%dir %{_pkglibdir}/interface
%dir %{_pkglibdir}/output
%dir %{_pkglibdir}/reader
%dir %{_pkglibdir}/scopes
%attr(755,root,root) %{_pkglibdir}/input/libcdda.so
%attr(755,root,root) %{_pkglibdir}/input/libwav.so
%attr(755,root,root) %{_pkglibdir}/output/liboss_out.so
%attr(755,root,root) %{_pkglibdir}/output/libnull_out.so
%attr(755,root,root) %{_pkglibdir}/reader/libfile.so
%attr(755,root,root) %{_pkglibdir}/reader/libhttp.so
%{_mandir}/man*/*
%{_desktopdir}/%{name}.desktop

%ifarch sparc
%attr(755,root,root) %{_pkglibdir}/output/libsparc_out.so
%endif

%files daemon
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/interface/libdaemon_interface.so

%files interface-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/interface/libgtk_interface.so

%files interface-text
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/interface/libtext_interface.so

%files interface-xosd
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/interface/libxosd_interface.so

%files input-audiofile
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/input/libaf.so

%files input-flac
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/input/libflac_in.so

%files input-mad
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/input/libmad_in.so

%files input-mikmod
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/input/libmod.so

%files input-sndfile
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/input/libsndfile_in.so

%files input-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/input/libvorbis_in.so

%files output-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/output/libalsa_out.so

%files output-esound
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/output/libesound_out.so

%files output-jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/output/libjack_out.so

%files output-nas
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/output/libnas_out.so

%files scopes-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/scopes/libblurscope.so
%attr(755,root,root) %{_pkglibdir}/scopes/liblevelmeter.so
%attr(755,root,root) %{_pkglibdir}/scopes/liblogbarfft.so
%attr(755,root,root) %{_pkglibdir}/scopes/libmonoscope.so
%attr(755,root,root) %{_pkglibdir}/scopes/libspacescope.so
%attr(755,root,root) %{_pkglibdir}/scopes/libsynaescope.so

%files scopes-opengl
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/scopes/liboglspectrum.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libalsaplayer.so
%{_libdir}/libalsaplayer.la
%{_includedir}/alsaplayer
%{_pkgconfigdir}/alsaplayer.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libalsaplayer.a
