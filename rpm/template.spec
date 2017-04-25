Name:           ros-lunar-socketcan-bridge
Version:        0.7.2
Release:        0%{?dist}
Summary:        ROS socketcan_bridge package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/socketcan_bridge
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-can-msgs
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-socketcan-interface
BuildRequires:  ros-lunar-can-msgs
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-roslint
BuildRequires:  ros-lunar-rostest
BuildRequires:  ros-lunar-rosunit
BuildRequires:  ros-lunar-socketcan-interface

%description
Provides nodes to convert messages from SocketCAN to a ROS Topic and vice versa.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Tue Apr 25 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.2-0
- Autogenerated by Bloom

