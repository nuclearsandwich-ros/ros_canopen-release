Name:           ros-kinetic-canopen-motor-node
Version:        0.7.1
Release:        0%{?dist}
Summary:        ROS canopen_motor_node package

Group:          Development/Libraries
License:        LGPLv3
URL:            http://wiki.ros.org/canopen_motor_node
Source0:        %{name}-%{version}.tar.gz

Requires:       muParser-devel
Requires:       ros-kinetic-canopen-402
Requires:       ros-kinetic-canopen-chain-node
Requires:       ros-kinetic-controller-manager
Requires:       ros-kinetic-controller-manager-msgs
Requires:       ros-kinetic-filters
Requires:       ros-kinetic-hardware-interface
Requires:       ros-kinetic-joint-limits-interface
Requires:       ros-kinetic-urdf
BuildRequires:  muParser-devel
BuildRequires:  ros-kinetic-canopen-402
BuildRequires:  ros-kinetic-canopen-chain-node
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-controller-manager
BuildRequires:  ros-kinetic-controller-manager-msgs
BuildRequires:  ros-kinetic-filters
BuildRequires:  ros-kinetic-hardware-interface
BuildRequires:  ros-kinetic-joint-limits-interface
BuildRequires:  ros-kinetic-urdf

%description
This package extends the canopen_chain_node with specialized handling for
canopen_402 devices. It facilitates interface abstraction with ros_control.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Mar 20 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.1-0
- Autogenerated by Bloom

* Thu Dec 15 2016 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.0-0
- Autogenerated by Bloom

